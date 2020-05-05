SELECT toxins.county,
min_cancer.cases, max_cancer.cases,
toxins.voc, toxins.nox, toxins.co, toxins.co2, toxins.particulate, toxins.pm10, toxins.pm25, toxins.haps, toxins.so2
FROM toxins
LEFT JOIN(
	SELECT cancers.county as countys, cancers.cancer, cancers.cases, toxins.county
	FROM cancers,toxins
	WHERE cancers.cases != 0
	AND cancers.county = toxins.county
	AND cancers.cancer LIKE 'Lung and Bronchus'
	ORDER BY cancers.cases ASC
	LIMIT 1
) AS min_cancer
ON toxins.county = min_cancer.countys
LEFT JOIN(
	SELECT cancers.county as countys, cancers.cancer, cancers.cases, toxins.county
	FROM cancers,toxins
	WHERE cancers.cases != 0
	AND cancers.county = toxins.county
	AND cancers.cancer LIKE 'Lung and Bronchus'
	ORDER BY cases DESC
	LIMIT 1
) AS max_cancer
ON toxins.county = max_cancer.countys
WHERE (min_cancer.cases IS NOT NULL OR max_cancer.cases IS NOT NULL);