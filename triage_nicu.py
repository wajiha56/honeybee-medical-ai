from config import settings

class TriageAndNICU:
    def __init__(self):
        # Initial NICU Capacity
        self.nicu_capacity = {"incubators": 5, "ventilators": 2}
        self.current_token = 0

    def check_red_flags(self, message_text: str) -> bool:
        # Multi-dialect red-flag safety interrupt (Urdu Nastaliq, Roman Urdu, English)
        message_lower = message_text.lower()
        for flag in settings.TRIAGE_RED_FLAGS:
            if flag in message_lower:
                return True
        return False

    def get_emergency_directions(self):
        return "🚨 EMERGENCY ALERT: Baraye meharbani foran qareebi Emergency Room (ER) jayen!"

    def process_staff_command(self, command_text: str):
        # Front-Desk Staff WhatsApp Command Bot Overrides
        cmd = command_text.strip().lower()
        
        if cmd.startswith(('/next', '/اگلا')):
            self.current_token += 1
            return f"Token updated. Now serving: {self.current_token}"
            
        elif cmd.startswith(('/token', '/ٹوکن')):
            parts = cmd.split()
            if len(parts) > 1 and parts[1].isdigit():
                self.current_token = int(parts[1])
                return f"Token manually set to: {self.current_token}"
                
        elif cmd.startswith(('/nicu', '/نرسری')):
            # Format: /nicu <inc> <vent>
            parts = cmd.split()
            if len(parts) == 3:
                self.nicu_capacity["incubators"] = int(parts[1])
                self.nicu_capacity["ventilators"] = int(parts[2])
                return f"NICU Updated: Incubators: {parts[1]}, Ventilators: {parts[2]}"
                
        elif cmd.startswith(('/status', '/صورتحال')):
            return f"Current Token: {self.current_token} | NICU Incubators: {self.nicu_capacity['incubators']} | Ventilators: {self.nicu_capacity['ventilators']}"
            
        return "Command na-maloom hai."

triage_engine = TriageAndNICU()