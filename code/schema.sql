DROP TABLE IF EXISTS toxins_raw;
DROP TABLE IF EXISTS toxins_avg;

CREATE TABLE toxins_raw(
	year SMALLINT,
	county VARCHAR(255),
	municipality VARCHAR(255),
	facility TEXT,
	voc real,
	nox real,
	co real,
	co2 real,
	particulate real,
	pm10 real,
	pm25 real,
	haps real,
	so2 real
);

CREATE TABLE toxins_avg(
	county VARCHAR(255),
	voc real,
	nox real,
	co real,
	co2 real,
	particulate real,
	pm10 real,
	pm25 real,
	haps real,
	so2 real
)