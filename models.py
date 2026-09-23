from pydantic import BaseModel
from typing import Optional, List
from datetime import date

# --- Pydantic Schemas (API Data Validation) ---
class PatientBase(BaseModel):
    parent_phone: str
    child_name: str
    date_of_birth: date
    gender: str

class AppointmentCreate(BaseModel):
    patient_phone: str
    doctor_id: str
    hospital_name: str
    appointment_date: date
    token_number: int

class WebhookPayload(BaseModel):
    object: str
    entry: List[dict]

# --- Database Layer ---
class MedicalDatabaseRepo:
    def __init__(self, db_path="medical_engine.db"):
        self.db_path = db_path
        
    def get_connection(self):
        import sqlite3
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        return conn

    def setup_database(self, schema_file="schema.sql"):
        # Yeh function aapki schema.sql file ko run kar ke tables banayega
        import os
        if os.path.exists(schema_file):
            with open(schema_file, 'r', encoding='utf-8') as f:
                schema_script = f.read()
            conn = self.get_connection()
            
            # Error handling add ki gayi hai taake bar bar reload par server crash na ho
            try:
                conn.executescript(schema_script)
            except Exception as e:
                pass # Agar tables pehle se majood hain toh error ignore ho jayega
                
            conn.commit()
            conn.close()

db_repo = MedicalDatabaseRepo()
