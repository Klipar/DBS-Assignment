-- SET enable_indexscan = OFF;
-- SET enable_bitmapscan = OFF;

CREATE INDEX idx_screenings_film_start ON screenings(film_id, start_time);
CREATE INDEX idx_sales_screening_id ON sales(screening_id);

-- Execution Time	5.472 ms	2.589 ms	53%
-- Planning Time	1.074 ms	0.759 ms	29%
-- Total Time	    6.546 ms	3.348 ms	49%