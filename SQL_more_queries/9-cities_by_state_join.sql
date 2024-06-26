-- List all cities contained in the database hbtn_0e_4_us by join between the cities and states tables
SELECT cities.id, cities.name, states.name
FROM cities JOIN states ON cities.state_id = states.id
ORDER BY cities.id ASC;
