-- Converts database hbtn_0c_0 to UTF8
-- thus utf8mb4, collate utf8mb4_unicode_ci
ALTER DATABASE hbtn_0c_0
CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

ALTER TABLE first_table
CHARACTER SET utf8;

ALTER TABLE first_table
MODIFY name CHARACTER SET utf8;
