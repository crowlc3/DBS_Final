SELECT toxins.county,
min_cancer.cancer, max_cancer.cancer, min_cancer.cases, max_cancer.cases,
toxins.voc, toxins.nox, toxins.co, toxins.co2, toxins.particulate, toxins.pm10, toxins.pm25, toxins.haps, toxins.so2
FROM toxins
LEFT JOIN(
	SELECT county, cancer, cases
	FROM cancers
	WHERE cases != 0
	AND cancer LIKE 'Leukemias'
	ORDER BY cases ASC
	LIMIT 1
) AS min_cancer
ON toxins.county = min_cancer.county
LEFT JOIN(
	SELECT county, cancer, cases
	FROM cancers
	WHERE cases != 0
	AND cancer LIKE 'Leukemias'
	ORDER BY cases DESC
	LIMIT 1
) AS max_cancer
ON toxins.county = max_cancer.county
WHERE (min_cancer.cases IS NOT NULL OR max_cancer.cases IS NOT NULL);