-- 1. Tenant Master (Clinics / Practice Networks)
CREATE TABLE tenants (
    tenant_id VARCHAR(64) PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- 2. Doctors
CREATE TABLE doctors (
    doctor_id VARCHAR(64) PRIMARY KEY,
    tenant_id VARCHAR(64) REFERENCES tenants(tenant_id),
    name_en VARCHAR(255) NOT NULL,
    name_ur VARCHAR(255) NOT NULL,
    specialty_en VARCHAR(255) NOT NULL,
    specialty_ur VARCHAR(255) NOT NULL,
    phone_number VARCHAR(32) NOT NULL,
    default_fee NUMERIC(10, 2),
    active BOOLEAN DEFAULT TRUE
);

-- 3. Hospital Branches & Weekly Rosters
CREATE TABLE hospital_branches (
    branch_id VARCHAR(64) PRIMARY KEY,
    doctor_id VARCHAR(64) REFERENCES doctors(doctor_id),
    hospital_name_en VARCHAR(255) NOT NULL,
    hospital_name_ur VARCHAR(255) NOT NULL,
    branch_name_en VARCHAR(255),
    branch_name_ur VARCHAR(255),
    address_en TEXT NOT NULL,
    address_ur TEXT NOT NULL,
    google_maps_url TEXT,
    consultation_fee NUMERIC(10, 2),
    active BOOLEAN DEFAULT TRUE
);

CREATE TABLE doctor_schedules (
    schedule_id SERIAL PRIMARY KEY,
    branch_id VARCHAR(64) REFERENCES hospital_branches(branch_id),
    day_of_week INT NOT NULL, -- 0=Monday, 6=Sunday
    start_time TIME NOT NULL,
    end_time TIME NOT NULL,
    max_tokens_per_session INT DEFAULT 35
);

-- 4. Live OPD Queue Sessions
CREATE TABLE queue_sessions (
    session_id VARCHAR(64) PRIMARY KEY,
    branch_id VARCHAR(64) REFERENCES hospital_branches(branch_id),
    session_date DATE NOT NULL,
    current_token_serving INT DEFAULT 0,
    total_tokens_issued INT DEFAULT 0,
    is_active BOOLEAN DEFAULT TRUE
);

-- 5. NICU Incubator & Ventilator Inventory
CREATE TABLE nicu_capacity (
    facility_id VARCHAR(64) PRIMARY KEY,
    branch_id VARCHAR(64) REFERENCES hospital_branches(branch_id),
    incubators_total INT DEFAULT 0,
    incubators_available INT DEFAULT 0,
    ventilators_total INT DEFAULT 0,
    ventilators_available INT DEFAULT 0,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- 6. Patients & Growth Records
CREATE TABLE patients (
    patient_id VARCHAR(64) PRIMARY KEY,
    parent_phone VARCHAR(32) NOT NULL UNIQUE,
    child_name VARCHAR(255) NOT NULL,
    date_of_birth DATE NOT NULL,
    gender VARCHAR(16) NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE growth_measurements (
    measurement_id SERIAL PRIMARY KEY,
    patient_id VARCHAR(64) REFERENCES patients(patient_id),
    recorded_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    age_in_months NUMERIC(5, 2) NOT NULL,
    weight_kg NUMERIC(5, 2) NOT NULL,
    length_cm NUMERIC(5, 2)
);

-- 7. Appointments
CREATE TABLE appointments (
    appointment_id VARCHAR(64) PRIMARY KEY,
    patient_phone VARCHAR(32) NOT NULL,
    doctor_id VARCHAR(64) REFERENCES doctors(doctor_id),
    hospital_name VARCHAR(255) NOT NULL,
    appointment_date DATE NOT NULL,
    token_number INT NOT NULL,
    status VARCHAR(32) DEFAULT 'CONFIRMED',
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- 8. Triage Audit & Safety Events Log
CREATE TABLE triage_events (
    event_id SERIAL PRIMARY KEY,
    patient_phone VARCHAR(32) NOT NULL,
    message_text TEXT NOT NULL,
    detected_keywords TEXT NOT NULL,
    triage_level VARCHAR(32) NOT NULL,
    timestamp TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);