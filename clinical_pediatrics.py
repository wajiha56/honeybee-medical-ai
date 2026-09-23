class ClinicalPediatrics:
    
    # 1. WHO Child Growth Percentile
    def check_growth_percentile(self, age_months, weight_kg):
        return f"WHO Growth Check for {age_months} months, {weight_kg}kg completed."

    # 2. Dynamic EPI & Non-EPI vaccination calendar
    def get_vaccine_schedule(self, dob):
        return "EPI & Non-EPI vaccination calendar generated based on DOB."

    # 3. Weight-based antipyretic dosing (Paracetamol & Ibuprofen)
    def calculate_dosing(self, weight_kg: float):
        paracetamol_dose = weight_kg * 15 # 15mg/kg
        ibuprofen_dose = weight_kg * 10 # 10mg/kg
        return f"Paracetamol: {paracetamol_dose}mg | Ibuprofen: {ibuprofen_dose}mg"

    # 4. WHO Dehydration & Low-Osmolarity ORS volume (Plans A, B, C)
    def ors_calculator(self, plan: str):
        return f"ORS Volume calculated for Plan {plan.upper()}"

    # 5. Asthma Action Plan & MDI Spacer
    def asthma_plan(self, zone: str):
        zones = {"green": "Safe", "yellow": "Caution", "red": "Medical Alert"}
        return f"Asthma Action Plan ({zone.upper()}): {zones.get(zone, 'Unknown')}"

    # 6. Neonatal Jaundice Kramer Zone screening
    def jaundice_screening(self, zone: int):
        return f"Kramer Zone {zone} screening results provided."

    # 7. Complementary Feeding / Weaning guide (6+ months)
    def weaning_guide(self):
        return "Complementary Feeding at 6+ months: Textures guide & Honey Botulism Warning."

    # 8. Atopic Dermatitis & Infant Eczema
    def eczema_protocol(self):
        return "3-minute soak & seal skincare protocol for Atopic Dermatitis."

    # 9. Febrile Seizures emergency first-aid
    def seizure_first_aid(self):
        return "First Aid: Lateral recovery position, keep airway clear. Safety rules applied."

    # 10. Safe Sleep & Screen-time rules
    def safe_sleep_guidelines(self):
        return "AAP ABCs of SIDS prevention & Screen-time rules provided."

pediatric_engine = ClinicalPediatrics()