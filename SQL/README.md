# Introduction

This folder contains a single SQL file named biguqery_export.sql

This SQL code is intended to be run as a Scheduled Query on an interval and will export a table out to a GCS bucket.

## Customization Notes
There are two TODO notes in the code itself stating where customizations need to be done to match to your bucket name and
BigQuery source location.

Also in the final lines of the query it does a SELECT * which might need to be changed if you do not wish to grab all
columns in the source table. This is actually highly recommended to be changed to reduce costs here, unless there is an
explicit need for all columns in that table.

## Utilizing as a non-Scheduled Query
There is a commented out section before the main code that declares the hour variable that can be uncommented (make sure
to comment out the previous declaration of hour) to utilize this as a non-Scheduled Query.