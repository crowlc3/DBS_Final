DROP TABLE IF EXISTS toxins_raw;
DROP TABLE IF EXISTS toxins;
DROP TABLE IF EXISTS cancers;
DROP TABLE IF EXISTS toxins_avg;
DROP TABLE IF EXISTS cancers_county;

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

CREATE TABLE toxins(
	county VARCHAR(255) PRIMARY KEY,
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

CREATE TABLE cancers(
	county VARCHAR(255),
	cancer VARCHAR(255),
	cases INT,
	population INT, 
	age_adjusted_rate real,
	PRIMARY KEY (county, cancer)
);
