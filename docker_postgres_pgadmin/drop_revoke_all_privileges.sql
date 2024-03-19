REVOKE ALL PRIVILEGES ON ALL TABLES IN SCHEMA public FROM itversity_retail_user;
REVOKE ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public FROM itversity_retail_user;
REVOKE ALL PRIVILEGES ON ALL FUNCTIONS IN SCHEMA public FROM itversity_retail_user;
REVOKE ALL PRIVILEGES ON DATABASE itversity_retail_db FROM itversity_retail_user;
REVOKE ALL PRIVILEGES ON DATABASE itversity_retail_db FROM itversity_retail_user;
REVOKE ALL ON SCHEMA "public" FROM itversity_retail_user;

DROP OWNED BY itversity_retail_user;
DROP ROLE itversity_retail_user;
DROP USER itversity_retail_user;