from enum import Enum

class UserRole(str, Enum):
    ADMIN = "ADMIN"
    VOLUNTEER = "VOLUNTEER"


class ApprovalStatus(str, Enum):
    PENDING = "PENDING"
    APPROVED = "APPROVED"
    REJECTED = "REJECTED"


class EmergencyStatus(str, Enum):
    SEARCHING = "SEARCHING"
    ASSIGNED = "ASSIGNED"
    VOLUNTEER_EN_ROUTE = "VOLUNTEER_EN_ROUTE"
    COMPLETED = "COMPLETED"
    CANCELLED = "CANCELLED"


class AssignmentStatus(str, Enum):
    PENDING = "PENDING"
    ACCEPTED = "ACCEPTED"
    DECLINED = "DECLINED"
    EXPIRED = "EXPIRED"
    CANCELLED = "CANCELLED"
    ARRIVED = "ARRIVED"
    COMPLETED = "COMPLETED"


class OrganizationType(str, Enum):
    AMBULANCE = "AMBULANCE"
    RESCUE_TEAM = "RESCUE_TEAM"
    RED_CROSS = "RED_CROSS"
    FIRE_DEPARTMENT = "FIRE_DEPARTMENT"


class MedicalFacilityType(str, Enum):
    HOSPITAL = "HOSPITAL"
    CLINIC = "CLINIC"


class DevicePlatform(str, Enum):
    ANDROID = "ANDROID"
    
class NotificationStatus(str, Enum):
    PENDING = "PENDING"
    SENT = "SENT"
    DELIVERED = "DELIVERED"
    ACCEPTED = "ACCEPTED"
    DECLINED = "DECLINED"
    EXPIRED = "EXPIRED"
    FAILED = "FAILED"
    
