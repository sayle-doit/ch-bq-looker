# Introduction

This folder contains a single file named load_gcs_file_into_clickhouse.py

This python script acts as an Eventarc Cloud Function on Google Cloud that is triggered by
the finalized event on an object being written to a GCS bucket.

## Notes for setup_ch_client()
Before using ensure that you create the secrets required by the setup_ch_client() function. These are notated in the 
function comments.

It will use the default of always secure and port 9019 so those two values are optional.

## Notes for perform_load()
Before using ensure that you change the table_name variable value to the correct table name. Alternatively if you need 
to change up the SQL code to suit your needs. The code in there is very basic to handle the easiest case so there is a 
good chance it will need to be updated for more complex scenarios.

Another option is to Add a runtime environment variable with the table name in it and then modify the table_name 
variable to use that value in the case you utilize this Cloud Function for multiple Cloud Functions or other use cases.