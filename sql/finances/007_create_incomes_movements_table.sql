CREATE TABLE incomes_movements (
    movement_id INT UNSIGNED NOT NULL,
    income_id INT UNSIGNED NOT NULL,
    PRIMARY KEY (movement_id , income_id),
    CONSTRAINT fk_income_movement_id FOREIGN KEY (movement_id)
        REFERENCES movements (id)
        ON UPDATE CASCADE ON DELETE RESTRICT,
    CONSTRAINT fk_movement_income_id FOREIGN KEY (income_id)
        REFERENCES incomes (id)
);