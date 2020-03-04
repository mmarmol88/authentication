CREATE DATABASE auth_backend;
CREATE USER auth_backenduser
WITH PASSWORD 'auth';
GRANT ALL PRIVILEGES ON DATABASE auth_backend TO auth_backenduser;