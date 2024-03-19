GRANT ALL ON DATABASE itversity_retail_db TO itversity_retail_user;

grant all privileges on database itversity_retail_db to itversity_retail_user;

-- But, none of these privileges permit the user to read data from the table.
-- Therefore, it requires the SELECT privilege. We resolve this permission denied error using the command.
-- The new_user was then able to read data from the table.
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO itversity_retail_user;

-- Similarly, we can also resolve the permission denied error by setting DEFAULT privileges to the user.
-- Here, we use the ALTER DEFAULT PRIVILEGES command to define the default access privileges.
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL ON TABLES TO itversity_retail_user;

-- This will be specific to the schema specified in the command. Also, to apply it to the entire database, we use the command,
ALTER DEFAULT PRIVILEGES GRANT ALL ON TABLES TO new_user;
