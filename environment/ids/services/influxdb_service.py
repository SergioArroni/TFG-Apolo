# ====================== Adversarial Machine Learning Protected Intrusion Detection System ======================
#
# InfluxDB service -> Functions to add data to an InfluxDB database.
#
# Author: Sergio Arroni Del Riego
#
# ================================================================================================================

# Imports
from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS


class InfluxDBService:
    def __init__(self) -> None:
        """
        Initialize the InfluxDBService class.

        Parameters:
            None
        Output:
            None
        """

    # Functions
    def get_influxdb_connection(self, url: str, token: str, org: str) -> InfluxDBClient:
        """
        Get an InfluxDB connection instance.

        Args:
            url: InfluxDB URL.
            token: InfluxDB token.
            org: InfluxDB organization.
        Returns:
            InfluxDB connection instance.
        """
        return InfluxDBClient(url=url, token=token, org=org)

    def close_influxdb_connection(self, influxdb_connection: InfluxDBClient) -> None:
        """
        Close an InfluxDB connection.

        Args:
            influxdb_connection: InfluxDB connection.
        Returns:
            None.
        """
        influxdb_connection.close()

    def add_influxdb_data(
        self,
        influxdb_connection: InfluxDBClient,
        bucket: str,
        measurement_name: str,
        value: float,
        tags: dict,
    ) -> None:
        """
        Add data to an InfluxDB database.

        Args:
            influxdb_connection: InfluxDB connection.
            measurement_name: InfluxDB measurement name.
            bucket: InfluxDB bucket.
            value: Value to add.
            tags: Tags to add.
        Returns:
            None.
        """
        write_api = influxdb_connection.write_api(write_options=SYNCHRONOUS)
        point = Point(measurement_name).field("score", value)
        for tag in tags:
            point.tag(tag, tags[tag])
        write_api.write(bucket=bucket, record=point)
        write_api.close()
