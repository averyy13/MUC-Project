-- Define application user roles
CREATE TYPE user_role AS ENUM (
    'ADMIN',
    'VOLUNTEER'
);

-- Define volunteer verification status managed by admin
CREATE TYPE approval_status AS ENUM (
    'PENDING',
    'APPROVED',
    'REJECTED'
);

-- Define the life cycle of a patient's emergency request
CREATE TYPE emergency_status AS ENUM (
    'SEARCHING',
    'ASSIGNED',
    'VOLUNTEER_EN_ROUTE',
    'COMPLETED',
    'CANCELLED'
);

-- Define the action status of a volunteer for an assignment
CREATE TYPE assignment_status AS ENUM (
    'PENDING',
    'ACCEPTED',
    'DECLINED',
    'EXPIRED',
    'CANCELLED',
    'ARRIVED',
    'COMPLETED'
);

-- Define types of emergency services for contacts
CREATE TYPE organization_type AS ENUM (
    'AMBULANCE',
    'RESCUE_TEAM',
    'RED_CROSS',
    'FIRE_DEPARTMENT'
);

-- Define types of medical buildings
CREATE TYPE medical_facility_type AS ENUM (
    'HOSPITAL',
    'CLINIC'
);

-- Define target device platform for FCM push notifications
CREATE TYPE device_platform AS ENUM (
    'ANDROID'
);

CREATE TYPE notification_status AS ENUM (
    'PENDING',
    'SENT',
    'DELIVERED',
    'ACCEPTED',
    'DECLINED',
    'EXPIRED',
    'FAILED'
);

