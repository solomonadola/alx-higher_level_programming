-- this script creates table unique_id
-- and make the id unique
CREATE TABLE IF NOT EXISTS unique_id (id INT UNIQUE DEFAULT 1, name VARCHAR(256));