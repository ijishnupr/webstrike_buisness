CREATE TABLE user_role(
    id SERIAL PRIMARY KEY,
    role VARCHAR(50) NOT NULL UNIQUE
);

CREATE TABLE app_user (
    id SERIAL PRIMARY KEY,
    user_role_id INT REFERENCES user_role(id),
    fullname VARCHAR(100) NOT NULL,
    user_code VARCHAR(100) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    is_active BOOLEAN DEFAULT TRUE
);