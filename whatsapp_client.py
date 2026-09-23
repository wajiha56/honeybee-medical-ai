import hmac
import hashlib
import requests
from config import settings

class WhatsAppClient:
    def __init__(self):
        self.api_url = f"https://graph.facebook.com/v20.0/{settings.PHONE_NUMBER_ID}/messages"
        self.headers = {
            "Authorization": f"Bearer {settings.WHATSAPP_TOKEN}",
            "Content-Type": "application/json"
        }

    # Cryptographic HMAC-SHA256 signature verification ('X-Hub-Signature-256')
    def verify_signature(self, payload: bytes, signature_header: str) -> bool:
        if not signature_header:
            return False
        
        expected_hash = hmac.new(
            settings.WHATSAPP_APP_SECRET.encode(),
            payload,
            hashlib.sha256
        ).hexdigest()
        
        expected_signature = f"sha256={expected_hash}"
        return hmac.compare_digest(expected_signature, signature_header)

    # Approved Meta HSM templates for bypassing 24-hour window
    def send_hsm_template(self, to_phone: str, template_name: str, components: list):
        # Templates: dr_tayyab_review_request_ur, pediatric_vax_followup_ur, nicu_discharge_check_ur
        data = {
            "messaging_product": "whatsapp",
            "to": to_phone,
            "type": "template",
            "template": {
                "name": template_name,
                "language": {"code": "ur"},
                "components": components
            }
        }
        # In production, yeh Meta API ko hit karega:
        # response = requests.post(self.api_url, headers=self.headers, json=data)
        # return response.json()
        return {"status": "Template sent successfully (Simulated)"}

    # Webhook idempotency ('wamid' tracking)
    def track_wamid(self, wamid: str) -> bool:
        # Yahan wamid database mein save ho kar check hoga taake message repeat na ho
        return True

wa_client = WhatsAppClient()