-- Generate UUIDs for primary keys
CREATE EXTENSION IF NOT EXISTS pgcrypto;

-- Geographic data and spatial queries (Required for tracking & distance calculations)
CREATE EXTENSION IF NOT EXISTS postgis;

-- Better text searching (Optional / Reserved for future use)
-- CREATE EXTENSION IF NOT EXISTS pg_trgm;

-- Verification query to ensure extensions are installed successfully
SELECT extname
FROM pg_extension
WHERE extname IN ('pgcrypto', 'postgis');