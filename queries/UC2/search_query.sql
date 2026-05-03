SELECT DISTINCT
  f.id,
  f.name,
  f.duration,
  f.age_group

FROM
  films AS f

JOIN actors_films AS af ON af.film_id = f.id
JOIN actors AS a ON af.actor_id = a.id AND a.name = '{{name}}' AND a.surname = '{{surname}}'

JOIN films_genres AS fg ON fg.film_id = f.id
JOIN genres AS g ON g.id = fg.genre_id AND g.name = '{{genre}}'

JOIN films_studios AS fs ON fs.film_id = f.id
JOIN studios AS s ON s.id = fs.studio_id AND s.name = '{{studio}}'