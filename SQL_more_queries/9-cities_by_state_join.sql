-- lists all cities contained in the database
-- display: cities.id - cities.name - states.name

SELECT cities.id cities.name states.name
FROM cities
LEFT JOIN states ON cities.state_id = states.id