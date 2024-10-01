-- Import the table from the provided dump file (replace 'metal_bands.sql.zip' with the actual path)
IMPORT FILE 'metal_bands.sql.zip';

SELECT band_name,
       DATEDIFF(YEAR, formed, split) AS lifespan
FROM metal_bands
WHERE main_style = 'Glam rock';

ORDER BY lifespan DESC;