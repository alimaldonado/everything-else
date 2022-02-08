-- how many times in a year you receive the ammount
ALTER TABLE incomes ADD COLUMN year_intervals SMALLINT AFTER is_regular;