--Creates indexes for emergency routing performance optimization.

-- ======================================================
-- 1. USERS INDEXES
-- ======================================================
-- Optimize user filtering by their role (Admin vs Volunteer)
CREATE INDEX idx_users_role ON users(role);

-- ======================================================
-- 2. VOLUNTEERS INDEXES
-- ======================================================
-- Fast filtering for dashboard admin approvals
CREATE INDEX idx_volunteers_status ON volunteers(approval_status);

-- Fast tracking for volunteers who are marked as available
CREATE INDEX idx_volunteers_availability ON volunteers(availability);

-- Spatial index for volunteer home bases (Crucial for regional mapping)
CREATE INDEX idx_volunteers_home_location ON volunteers USING GIST(home_location);

-- NOTE: Removed idx_volunteers_user because user_id is already UNIQUE, 
-- which automatically creates a B-Tree index in PostgreSQL.

-- ======================================================
-- 3. DEVICE TOKENS INDEXES
-- ======================================================
-- Fast lookup when targeted push notifications need to find a volunteer's phone token
CREATE INDEX idx_device_tokens_volunteer ON device_tokens(volunteer_id);

-- ======================================================
-- 4. EMERGENCY CONTACTS INDEXES
-- ======================================================
-- Optimize sorting by service types (Ambulance, Fire Department, etc.)
CREATE INDEX idx_emergency_contacts_type ON emergency_contacts(type);
CREATE INDEX idx_emergency_contacts_active ON emergency_contacts(is_active);

-- Spatial index to find the nearest non-profit rescue organizations
CREATE INDEX idx_emergency_contacts_location ON emergency_contacts USING GIST(location);

-- ======================================================
-- 5. MEDICAL FACILITIES INDEXES
-- ======================================================
CREATE INDEX idx_medical_facilities_type ON medical_facilities(type);
CREATE INDEX idx_medical_facilities_active ON medical_facilities(is_active);

-- Spatial index to find nearby Hospitals/Clinics instantly on the map
CREATE INDEX idx_medical_facilities_location ON medical_facilities USING GIST(location);

-- ======================================================
-- 6. FIRST AID INDEXES
-- ======================================================
-- Fast querying for step instructions when an emergency category is selected
CREATE INDEX idx_first_aid_category ON first_aid_steps(category_id);

-- Composite index to load first-aid steps sequentially (Step 1, Step 2, Step 3...)
CREATE INDEX idx_first_aid_step ON first_aid_steps(category_id, step_number);

-- ======================================================
-- 7. EMERGENCY REQUESTS INDEXES
-- ======================================================
CREATE INDEX idx_requests_status ON emergency_requests(status);
CREATE INDEX idx_requests_created ON emergency_requests(created_at);
CREATE INDEX idx_requests_category ON emergency_requests(category_id);

-- Spatial index to track the patient's active emergency location point
CREATE INDEX idx_requests_location ON emergency_requests USING GIST(location);

-- ======================================================
-- 8. VOLUNTEER ASSIGNMENTS INDEXES
-- ======================================================
CREATE INDEX idx_assignments_request ON volunteer_assignments(request_id);
CREATE INDEX idx_assignments_volunteer ON volunteer_assignments(volunteer_id);
CREATE INDEX idx_assignments_status ON volunteer_assignments(status);
CREATE INDEX idx_assignments_round ON volunteer_assignments(notification_round);
CREATE INDEX idx_assignments_expire ON volunteer_assignments(expires_at);

-- ======================================================
-- 9. CURRENT VOLUNTEER LOCATIONS INDEXES
-- ======================================================
-- High-frequency Spatial Index to locate active moving responders in real-time
CREATE INDEX idx_current_locations ON current_volunteer_locations USING GIST(location);

-- ======================================================
-- 10. ADVANCED COMPOSITE INDEXES (Multi-Column)
-- ======================================================
-- Fast admin filtering to isolate approved and currently active volunteers
CREATE INDEX idx_volunteers_status_availability ON volunteers(approval_status, availability);

-- Fast assignment lookup to query active dispatches
CREATE INDEX idx_assignment_request_status ON volunteer_assignments(request_id, status);

-- Fast background workers checking for expired request waves
CREATE INDEX idx_assignment_pending_expire ON volunteer_assignments(status, expires_at);

-- ======================================================
-- VERIFY INDEXES
-- ======================================================
-- Run this query to confirm all B-Tree and GIST indexes are active
SELECT
    schemaname,
    tablename,
    indexname
FROM pg_indexes
WHERE schemaname = 'public'
ORDER BY tablename, indexname;