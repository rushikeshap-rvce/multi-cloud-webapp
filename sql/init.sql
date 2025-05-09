CREATE DATABASE multicloud;
USE multicloud;
CREATE TABLE messages (
  id INT AUTO_INCREMENT PRIMARY KEY,
  content VARCHAR(255)
);
INSERT INTO messages (content) VALUES ('Hello from GCP'), ('Welcome to Multi-Cloud');
