-- Select all bands with Glam rock as their main style, ranked by longevity
SELECT 
    band_name, 
    -- Calculate lifespan based on 'split' and 'formed' years. If still active, use the current year.
    CASE 
        WHEN split IS NULL THEN YEAR(CURDATE()) - formed
        ELSE split - formed 
    END AS lifespan
FROM 
    bands
WHERE 
    main_style = 'Glam rock'
ORDER BY 
    lifespan DESC;