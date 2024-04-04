import clickhouse_connect
import functions_framework
import os

from cloudevents.http import CloudEvent


@functions_framework.cloud_event
def gcs_trigger(cloud_event: CloudEvent) -> tuple:
    """
        This function is triggered by a change in a storage bucket.
        Args:
            cloud_event: The CloudEvent that triggered this function.
        Returns:
            The event ID, event type, bucket, name, metageneration, and timeCreated.
        """

    # Used Google's example as reference for this function:
    # https://github.com/GoogleCloudPlatform/python-docs-samples/blob/HEAD/functions/v2/storage/main.py

    data = cloud_event.data
    bucket = data["bucket"]
    filename = data["name"]

    # Set up the ClickHouse client and perform the loading of data
    client = setup_ch_client()
    perform_load(client=client, bucket=bucket, filename=filename)

    return


def setup_ch_client() -> clickhouse_connect.driver.client:
    # Get the needed connection info from Secrets Manager
    # It is recommended to use Secret Manager for this and NOT hardcode them below

    """
        Make sure you have created the secret (default name is clickhouse)
        and exposed them as environment variables to this Cloud Function before
        running this it will throw an error.

        This code expects environment variables with these names (types and default value in parentheses):
        "host" (string)
        "port" (string, 9019)
        "secure" (boolean, True)
        "username" (string)
        "password" (string)
    """

    # Get the credentials from the passed in environment variables to the Cloud Function
    host = os.environ.get['host']
    port = os.environ.get('port', 9019)
    secure = os.environ.get("secure", True)
    username = os.environ.get["username"]
    password = os.environ.get["password"]

    ch_client = clickhouse_connect.get_client(host=host,
                                              port=port,
                                              secure=secure,
                                              username=username,
                                              password=password)
    return ch_client


def perform_load(ch_client, bucket, filename):
    # If needing to do any custom code before loads such as choosing different tables do it here

    # Make sure you change this table name to the correct one first :)
    table_name = "table"

    insert_sql = f"""INSERT INTO {table_name}
        SELECT *
        FROM
            s3Cluster('default', 'https://storage.googleapis.com/{bucket}/{filename}')"""
    ch_client.command(insert_sql)

    return
