import httpx
from groq import Groq
from fastapi import FastAPI, Request, HTTPException
from config import settings
from models import db_repo

# Groq AI ko configure karna (using GROQ_API_KEY from config/settings)
groq_client = Groq(api_key=settings.GROQ_API_KEY)

app = FastAPI(title="Honeybee Medical AI Engine", version="1.0.0")

@app.on_event("startup")
def startup_event():
    db_repo.setup_database()

@app.get("/")
async def root():
    return {"status": "online", "message": "Honeybee Medical Engine is running 100% with Groq AI!"}

@app.get("/webhook")
async def verify_webhook(request: Request):
    mode = request.query_params.get("hub.mode")
    token = request.query_params.get("hub.verify_token")
    challenge = request.query_params.get("hub.challenge")

    if mode and token:
        if mode == "subscribe" and token == settings.WHATSAPP_VERIFY_TOKEN:
            return int(challenge)
        raise HTTPException(status_code=403, detail="Token mismatch. Verification failed.")
    raise HTTPException(status_code=400, detail="Missing verification parameters.")

# --- WhatsApp Message + Groq AI Auto-Reply ---
@app.post("/webhook")
async def receive_message(request: Request):
    try:
        body = await request.json()
        
        for entry in body.get("entry", []):
            for change in entry.get("changes", []):
                value = change.get("value", {})
                messages = value.get("messages", [])
                
                if messages:
                    print("New WhatsApp Message Received!")
                    message_obj = messages[0]
                    from_number = message_obj.get("from")
                    
                    # Check karna ke kya message mein asal text-body maujood hai ya nahi
                    text_data = message_obj.get("text")
                    if not text_data:
                        print("Ignored non-text webhook event (like read/delivery receipt).")
                        continue
                        
                    user_message = text_data.get("body", "")
                    print(f"User Message: {user_message}")
                    
                    # Groq AI se medical jawab mangwana (Llama 3 model)
                    system_prompt = "You are Honeybee Medical AI, a helpful medical assistant for Dr. Tayyab Pediatric Clinic. Answer this patient's query politely and professionally in English, Urdu, or Roman Urdu."
                    
                    chat_completion = groq_client.chat.completions.create(
                        messages=[
                            {"role": "system", "content": system_prompt},
                            {"role": "user", "content": user_message}
                        ],
                        model="llama-3.3-70b-versatile",
                        temperature=0.7,
                    )
                    reply_text = chat_completion.choices[0].message.content
                    
                    # WhatsApp Cloud API credentials
                    url = f"https://graph.facebook.com/v18.0/{settings.PHONE_NUMBER_ID}/messages"
                    headers = {
                        "Authorization": f"Bearer {settings.WHATSAPP_TOKEN}",
                        "Content-Type": "application/json"
                    }
                    
                    data = {
                        "messaging_product": "whatsapp",
                        "to": from_number,
                        "type": "text",
                        "text": {"body": reply_text}
                    }
                    
                    async with httpx.AsyncClient() as client:
                        response = await client.post(url, json=data, headers=headers)
                        print("WhatsApp Send Response:", response.status_code, response.text)
                            
    except Exception as e:
        print("ERROR IN WEBHOOK REPLY:", str(e))

    return {"status": "success", "received": True}