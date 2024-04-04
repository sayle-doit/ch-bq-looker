-- NOTE for use:
-- Update the bucket name, project, dataset, and table names below before use
-- These are reflected in TODO comments below

-- This scheduled query is meant to be run every hour
-- It will run and dump all data from the past hour
-- into a folder in the bucket in parquet format.

-- Note that adding a pub/sub message notification will allow
-- triggering of additional processes after this such as loading
-- into ClickHouse.

-- Get the passed in run time of the query, subtract an hour, and "round" it to the hour mark
DECLARE hour TIMESTAMP DEFAULT TIMESTAMP_TRUNC(TIMESTAMP_SUB(@run_time, INTERVAL 1 HOUR), HOUR);

-- Note if running this outside of a Scheduled Query use this line below instead
-- of the one above so it will run correctly.
-- Make sure if you uncomment this line to comment out the above line.
--DECLARE hour TIMESTAMP DEFAULT TIMESTAMP_TRUNC(TIMESTAMP_SUB(CURRENT_TIMESTAMP(), INTERVAL 1 HOUR), HOUR);

-- TODO Update this to reflect your bucket name
DECLARE bucket_name STRING DEFAULT '<bucket_name>';

EXPORT DATA
  -- This path should be changed to a better format for real applications
  OPTIONS(uri=CONCAT('gs://', bucket_name, '/', CAST(hour AS STRING), '/*.parquet'),
    format='PARQUET',
    overwrite=FALSE ) AS

-- TODO Update the project, dataset, table, and timestamp field names in the below query
  SELECT *
  FROM
    `<project>.<dataset>.<table_name>`
  WHERE
    <timestamp_field> = TIMESTAMP_TRUNC(TIMESTAMP_SUB(hour, INTERVAL 1 HOUR), HOUR);