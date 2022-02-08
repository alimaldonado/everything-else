CREATE TABLE accounts (
    id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    account_number VARCHAR(255) NOT NULL,
    name VARCHAR(100) NOT NULL,
    institution_id INT unsigned NOT NULL,
    date_created DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    date_updated DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_account_institution FOREIGN KEY (institution_id)
        REFERENCES institutions (id)
        ON UPDATE CASCADE ON DELETE RESTRICT
);