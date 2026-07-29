-- ======================================================
-- 1. USERS TABLE
-- ======================================================
CREATE TABLE users (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    full_name VARCHAR(100) NOT NULL,
    phone VARCHAR(20) NOT NULL UNIQUE,
    email VARCHAR(120) UNIQUE,
    password_hash TEXT NOT NULL,
    role user_role NOT NULL,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

-- ======================================================
-- 2. VOLUNTEERS TABLE
-- ======================================================
CREATE TABLE volunteers (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID NOT NULL UNIQUE,
    nrc_number VARCHAR(30) NOT NULL,
    address TEXT NOT NULL,
    home_location GEOGRAPHY(Point,4326), -- PostGIS Spatial Point (Home base)
    certificate_url TEXT,
    approval_status approval_status NOT NULL DEFAULT 'PENDING',
    availability BOOLEAN NOT NULL DEFAULT FALSE,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    
    CONSTRAINT fk_volunteer_user FOREIGN KEY(user_id) REFERENCES users(id) ON DELETE CASCADE
);

-- ======================================================
-- 3. DEVICE TOKENS TABLE (For FCM Push Notifications)
-- ======================================================
CREATE TABLE device_tokens (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    volunteer_id UUID NOT NULL,
    fcm_token TEXT NOT NULL UNIQUE, -- Changed to UNIQUE to prevent duplicate push messaging bugs
    platform device_platform NOT NULL,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    
    CONSTRAINT fk_device_volunteer FOREIGN KEY(volunteer_id) REFERENCES volunteers(id) ON DELETE CASCADE
);

-- ======================================================
-- 4. EMERGENCY CONTACTS TABLE
-- ======================================================
CREATE TABLE emergency_contacts (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name_en VARCHAR(150) NOT NULL,
    name_mm VARCHAR(150) NOT NULL,
    phone VARCHAR(30) NOT NULL,
    type organization_type NOT NULL,
    location GEOGRAPHY(Point,4326) NOT NULL,
    is_active BOOLEAN NOT NULL DEFAULT TRUE,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

-- ======================================================
-- 5. MEDICAL FACILITIES TABLE
-- ======================================================
CREATE TABLE medical_facilities (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name_en VARCHAR(150) NOT NULL,
    name_mm VARCHAR(150) NOT NULL,
    phone VARCHAR(30),
    address_en TEXT,
    address_mm TEXT,
    type medical_facility_type NOT NULL,
    location GEOGRAPHY(Point,4326) NOT NULL,
    is_active BOOLEAN NOT NULL DEFAULT TRUE,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

-- ======================================================
-- 6. EMERGENCY CATEGORIES TABLE
-- ======================================================
CREATE TABLE emergency_categories (
    id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name_en VARCHAR(100) NOT NULL,
    name_mm VARCHAR(100) NOT NULL,
    priority SMALLINT NOT NULL DEFAULT 1
);

-- ======================================================
-- 7. FIRST AID STEPS TABLE
-- ======================================================
CREATE TABLE first_aid_steps (
    id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    category_id INTEGER NOT NULL,
    step_number SMALLINT NOT NULL,
    instruction_en TEXT NOT NULL,
    instruction_mm TEXT NOT NULL,
    
    CONSTRAINT fk_first_aid_category FOREIGN KEY(category_id) REFERENCES emergency_categories(id) ON DELETE CASCADE
);

-- ======================================================
-- 8. EMERGENCY REQUESTS TABLE (Patient Incident Reports)
-- ======================================================
CREATE TABLE emergency_requests (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),

    category_id INTEGER NOT NULL,

    requester_id UUID,

    description TEXT,

    location GEOGRAPHY(Point, 4326) NOT NULL,

    status emergency_status NOT NULL DEFAULT 'SEARCHING',

    assigned_volunteer_id UUID,

    assigned_rescue_contact_id UUID,

    accepted_at TIMESTAMPTZ,

    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),

    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),

    CONSTRAINT fk_request_category
        FOREIGN KEY (category_id)
        REFERENCES emergency_categories(id)
        ON DELETE RESTRICT,

    CONSTRAINT fk_request_user
        FOREIGN KEY (requester_id)
        REFERENCES users(id)
        ON DELETE SET NULL,

    CONSTRAINT fk_request_volunteer
        FOREIGN KEY (assigned_volunteer_id)
        REFERENCES volunteers(id)
        ON DELETE SET NULL,

    CONSTRAINT fk_request_rescue
        FOREIGN KEY (assigned_rescue_contact_id)
        REFERENCES emergency_contacts(id)
        ON DELETE SET NULL
);

-- ======================================================
-- 9. VOLUNTEER ASSIGNMENTS TABLE (Matching Requests to Responders)
-- ======================================================
CREATE TABLE volunteer_assignments (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    request_id UUID NOT NULL,
    volunteer_id UUID NOT NULL,
    notification_round INTEGER NOT NULL DEFAULT 1,
    status assignment_status NOT NULL DEFAULT 'PENDING',
    notified_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    expires_at TIMESTAMPTZ,
    accepted_at TIMESTAMPTZ,
    arrived_at TIMESTAMPTZ,
    completed_at TIMESTAMPTZ,
    
    CONSTRAINT fk_assignment_request FOREIGN KEY(request_id) REFERENCES emergency_requests(id) ON DELETE CASCADE,
    CONSTRAINT fk_assignment_volunteer FOREIGN KEY(volunteer_id) REFERENCES volunteers(id) ON DELETE CASCADE,
    CONSTRAINT unique_request_volunteer UNIQUE(request_id, volunteer_id)
);

-- ======================================================
-- 10. CURRENT VOLUNTEER LOCATIONS TABLE (High-frequency Live Tracking Base)
-- ======================================================
CREATE TABLE current_volunteer_locations (
    volunteer_id UUID PRIMARY KEY,
    location GEOGRAPHY(Point,4326) NOT NULL,
    speed DOUBLE PRECISION,
    heading DOUBLE PRECISION,
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    
    CONSTRAINT fk_current_location_volunteer FOREIGN KEY(volunteer_id) REFERENCES volunteers(id) ON DELETE CASCADE
);


-- ======================================================
-- 11. EMERGENCY NOTIFICATIONS TABLE (For Push Notifications to Volunteers)
-- ======================================================
CREATE TABLE emergency_notifications (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),

    emergency_request_id UUID NOT NULL
        REFERENCES emergency_requests(id) ON DELETE CASCADE,

    volunteer_id UUID NOT NULL
        REFERENCES volunteers(id) ON DELETE CASCADE,

    notification_order INTEGER NOT NULL,

    batch_number INTEGER NOT NULL,

    status notification_status NOT NULL DEFAULT 'PENDING',

    sent_at TIMESTAMPTZ,

    responded_at TIMESTAMPTZ,

    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),

    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);
-- ======================================================
-- AUTOMATIC TIMESTAMPTZ TRIGGERS CONFIGURATION
-- ======================================================
CREATE OR REPLACE FUNCTION trigger_set_timestamp()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = NOW();
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER set_timestamp_users BEFORE UPDATE ON users FOR EACH ROW EXECUTE FUNCTION trigger_set_timestamp();
CREATE TRIGGER set_timestamp_volunteers BEFORE UPDATE ON volunteers FOR EACH ROW EXECUTE FUNCTION trigger_set_timestamp();
CREATE TRIGGER set_timestamp_device_tokens BEFORE UPDATE ON device_tokens FOR EACH ROW EXECUTE FUNCTION trigger_set_timestamp();
CREATE TRIGGER set_timestamp_emergency_contacts BEFORE UPDATE ON emergency_contacts FOR EACH ROW EXECUTE FUNCTION trigger_set_timestamp();
CREATE TRIGGER set_timestamp_medical_facilities BEFORE UPDATE ON medical_facilities FOR EACH ROW EXECUTE FUNCTION trigger_set_timestamp();
CREATE TRIGGER set_timestamp_emergency_requests BEFORE UPDATE ON emergency_requests FOR EACH ROW EXECUTE FUNCTION trigger_set_timestamp();
CREATE TRIGGER set_timestamp_current_volunteer_locations BEFORE UPDATE ON current_volunteer_locations FOR EACH ROW EXECUTE FUNCTION trigger_set_timestamp();
CREATE TRIGGER set_timestamp_emergency_notifications BEFORE UPDATE ON emergency_notifications FOR EACH ROW EXECUTE FUNCTION trigger_set_timestamp();

-- Verification query to list all successfully created tables
SELECT table_name
FROM information_schema.tables
WHERE table_schema = 'public'
ORDER BY table_name;

