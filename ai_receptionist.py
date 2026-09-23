import os
from groq import Groq

class AIReceptionist:
    def __init__(self):
        # AI assistant configuration for English, Urdu, and Roman Urdu
        self.language_mode = "Bilingual"
        # Groq client initialization using environment variable
        api_key = os.environ.get("GROQ_API_KEY")
        self.client = Groq(api_key=api_key) if api_key else None

    def process_voice_note(self, audio_data: bytes) -> str:
        # Voice note placeholder (Groq text models handle text prompts, voice can be integrated via Whisper later if needed)
        return "Voice note processing ready via Groq pipeline."

    def inject_bilingual_prompt(self, user_query: str) -> str:
        # Bilingual prompt injector for Dr. Tayyab Pediatric Clinic using Groq API
        if not self.client:
            return "Error: GROQ_API_KEY is not set in environment variables."

        system_prompt = (
            "You are a professional and helpful AI receptionist for Dr. Tayyab Pediatric Clinic. "
            "Respond politely to medical and clinic-related queries. "
            "You can reply in English, Urdu, or Roman Urdu depending on what the user speaks."
        )

        try:
            chat_completion = self.client.chat.completions.create(
                messages=[
                    {
                        "role": "system",
                        "content": system_prompt
                    },
                    {
                        "role": "user",
                        "content": user_query,
                    }
                ],
                model="mixtral-8x7b-32768",  # Fast and reliable model on Groq
                temperature=0.7,
            )

            return chat_completion.choices[0].message.content
        except Exception as e:
            return f"Maazrat, abhi technical kharabi ki wajah se jawab nahi diya ja saka. Error: {str(e)}"

receptionist = AIReceptionist()