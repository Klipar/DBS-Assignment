SELECT
  s.id,
  s.start_time,
  s.language,
  h.name AS hall_name,
  h.capacity - COUNT (sl.id) AS free_seats

FROM
  screenings AS s

JOIN halls AS h on h.id = s.hall_id
LEFT JOIN sales AS sl ON sl.screening_id = s.id
WHERE s.film_id = 76
GROUP BY s.id, h.name, s.start_time, s.language, h.capacity
HAVING h.capacity > COUNT(sl.id)
ORDER BY start_time ASC