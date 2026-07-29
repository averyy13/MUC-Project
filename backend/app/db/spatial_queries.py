FIND_NEAREST_VOLUNTEERS = """
SELECT
    v.id AS volunteer_id,
    u.id AS user_id,
    u.full_name,
    u.phone,

    ST_Y(cvl.location::geometry) AS latitude,
    ST_X(cvl.location::geometry) AS longitude,

    ROUND(
        ST_Distance(
            cvl.location,
            ST_SetSRID(
                ST_MakePoint(:longitude, :latitude),
                4326
            )::geography
        )::numeric,
        2
    ) AS distance_meters

FROM volunteers v

JOIN users u
ON u.id = v.user_id

JOIN current_volunteer_locations cvl
ON cvl.volunteer_id = v.id

WHERE
    v.approval_status = 'APPROVED'
    AND
    v.availability = TRUE

ORDER BY distance_meters

LIMIT :limit;
"""


FIND_NEAREST_RESCUE_CONTACTS = """
SELECT
    id,
    name_en,
    name_mm,
    phone,
    type,

    ST_Y(location::geometry) AS latitude,
    ST_X(location::geometry) AS longitude,

    ROUND(
        ST_Distance(
            location,
            ST_SetSRID(
                ST_MakePoint(:longitude, :latitude),
                4326
            )::geography
        )::numeric,
        2
    ) AS distance_meters

FROM emergency_contacts

WHERE
    is_active = TRUE
    AND
    type IN ('AMBULANCE', 'RESCUE_TEAM')

ORDER BY distance_meters

LIMIT :limit;
"""


FIND_NEAREST_MEDICAL_FACILITIES = """
SELECT
    id,
    name_en,
    name_mm,
    phone,
    address_en,
    address_mm,
    type,

    ST_Y(location::geometry) AS latitude,
    ST_X(location::geometry) AS longitude,

    ROUND(
        ST_Distance(
            location,
            ST_SetSRID(
                ST_MakePoint(:longitude, :latitude),
                4326
            )::geography
        )::numeric,
        2
    ) AS distance_meters

FROM medical_facilities

WHERE
    is_active = TRUE

ORDER BY distance_meters

LIMIT :limit;
"""