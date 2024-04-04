# Introduction

Note that these queries go along with a blog series [1](https://www.doit.com/resources/the-bigquery-optimization-handbook-preparing-to-save/) 
[2](https://todo)
about utilizing ClickHouse as a "cache" for BigQuery in order to save on Looker (and other associated services) costs
written by Sayle Matthews of DoiT International.

This repo contains both SQL and python code going along with the processes described in the blog series.

## Structure

This repo is broken down into two directors: SQL and python

They are described below what is contained in each folder.

## SQL

The single file in this directory is a SQL file that will load the contents of a table into a GCS bucket.

It can be used as either a scheduled query or ran as standard SQL.

Read the README.md file in that directory for more details on exact usage.

## python

This directory contains python code that is intended to run as a Cloud Function triggered by an EventArc trigger on
a finalized event for a file in a GCS bucket. This Cloud Function will then load the file into a ClickHouse table.

Read the README.md file in that directory for exact usage of this code.