DROP TABLE IF EXISTS contacts;

CREATE TABLE contacts (
    id SERIAL PRIMARY KEY,
    name VARCHAR (255),
    phone_number BIGINT,
    email VARCHAR (255)
)