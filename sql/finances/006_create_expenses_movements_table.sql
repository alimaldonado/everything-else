CREATE TABLE expenses_movements (
    movement_id INT UNSIGNED NOT NULL,
    expense_id INT UNSIGNED NOT NULL,
    PRIMARY KEY (movement_id , expense_id),
    CONSTRAINT fk_expense_movement_id FOREIGN KEY (movement_id)
        REFERENCES movements (id)
        ON UPDATE CASCADE ON DELETE RESTRICT,
    CONSTRAINT fk_movement_expense_id FOREIGN KEY (expense_id)
        REFERENCES expenses (id)
);
