TRUNCATE TABLE CONTACTS;

ALTER SEQUENCE contacts_id_seq RESTART WITH 1;


INSERT INTO contacts(name, phone_number, email) VALUES ('Sam Delacruz',8034460449, 'sdmantha@gmail.com');
INSERT INTO contacts(name, phone_number, email) VALUES ('Antuan',8034460450, 'actuan@gmail.com');
INSERT INTO contacts(name, phone_number, email) VALUES ('Chu',8034460451, 'cdu@gmail.com');
INSERT INTO contacts(name, phone_number, email) VALUES ('Ariel ',8034460452, 'adiel@gmail.com');
