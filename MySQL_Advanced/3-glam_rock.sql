-- Import the table
IMPORT FILE 'metal_bands.sql.zip';

SELECT band_name,
       DATEDIFF(YEAR, formed, split) AS lifespan
FROM metal_bands
WHERE main_style = 'Glam rock';

ORDER BY lifespan DESC;