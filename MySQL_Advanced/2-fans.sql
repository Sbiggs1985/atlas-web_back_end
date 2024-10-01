-- Select the origin of bands and the total number of fans per country
SELECT 
    origin, 
    SUM(fans) AS nb_fans
FROM 
    bands
GROUP BY 
    origin
ORDER BY 
    nb_fans DESC;