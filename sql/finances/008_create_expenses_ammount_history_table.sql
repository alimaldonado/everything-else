CREATE TABLE expenses_ammount_history (
    id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    expense_id INT UNSIGNED NOT NULL,
    ammount DECIMAL(10 , 2 ) NOT NULL,
    date_dismissed DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_expenses_ammount_history_expense_id FOREIGN KEY (expense_id)
        REFERENCES expenses (id)
)