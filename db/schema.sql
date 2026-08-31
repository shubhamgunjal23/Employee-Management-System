CREATE TABLE IF NOT EXISTS items(
 id SERIAL PRIMARY KEY,
 name VARCHAR(200) NOT NULL,
 description TEXT,
 created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
INSERT INTO items(name,description) VALUES('Demo item','Created during local setup');
