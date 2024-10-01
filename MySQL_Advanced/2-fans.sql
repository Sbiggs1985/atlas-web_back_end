-- Select the origin of bands and the total number of fans per country, treating origins uniformly
SELECT 
    UPPER(origin) AS origin, 
    SUM(fans) AS nb_fans
FROM 
    bands
GROUP BY 
    UPPER(origin)
ORDER BY 
    nb_fans DESC;