class SchedulingEngine:
    def __init__(self):
        # Multi-Hospital data with fees and Google Maps routing
        self.hospitals = {
            "salamat": {
                "name_ur": "سلامت ہسپتال", 
                "fee": 1500, 
                "map_pin": "https://maps.google.com/?q=Salamat+Hospital"
            },
            "azeem": {
                "name_ur": "عظیم میڈیکل کمپلیکس", 
                "fee": 2000, 
                "map_pin": "https://maps.google.com/?q=Azeem+Medical+Complex"
            },
            "al_haj": {
                "name_ur": "الحاج ناصر خان", 
                "fee": 1000, 
                "map_pin": "https://maps.google.com/?q=Al+Haj+Nasir+Khan+Hospital"
            }
        }

    def get_clinic_info(self, clinic_key: str):
        clinic = clinic_key.lower().strip()
        if clinic in self.hospitals:
            return self.hospitals[clinic]
        return None

    def format_schedule_message(self, clinic_key: str):
        info = self.get_clinic_info(clinic_key)
        if info:
            return f"Clinic: {info['name_ur']}\nFee: Rs. {info['fee']}\nLocation: {info['map_pin']}"
        return "Clinic ki maloomat nahi mil saki."

scheduler = SchedulingEngine()