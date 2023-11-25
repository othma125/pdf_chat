CREATE DATABASE IF NOT EXISTS pdf_chat_db;
CREATE USER 'admin'@'localhost' IDENTIFIED BY 'admin_pwd';
GRANT ALL PRIVILEGES ON pdf_chat_db.* TO 'admin'@'localhost';

