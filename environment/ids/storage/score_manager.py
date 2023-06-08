# ========================== ScoreManager ==========================
#
#                   Author:  Sergio Arroni Del Riego
#
# ================================================================

# ==================> Imports
import pandas as pd
import os
import json
from services import InfluxDBService
from apolo.model_predict import ApoloPredict


# ==================> Classes
class ScoreManager:
    """ScoreManager

    This class is used to manage the scores of the requests.

    Attributes:
        ixs (object): InfluxDBService object
        ul (object): UtilsLoad object
        apolo (object): ApoloPredict object

    """

    def __init__(self) -> None:
        """__init__

        This method is used to initialize the ScoreManager class.

        Parameters:

        Output:
            None
        """
        self.ixs = InfluxDBService()
        self.apolo = ApoloPredict()

    def push_data_to_influxdb(
        self, last_element: list, url: str = "http://influxdb:8086", org: str = "TFG"
    ) -> None:
        """push_data_to_influxdb

        This method is used to push the data to the InfluxDB database.

        Parameters:
            last_element: Last element of the Redis list.
            url: InfluxDB url.
            org: InfluxDB organization.
        Output:
            None
        """

        # Get an InfluxDB connection
        influxdb_connection = self.ixs.get_influxdb_connection(
            url=url,
            token=os.environ.get("INFLUXDB_TOKEN"),
            org=org,
        )
        # Add the last element of the Redis list to the InfluxDB database
        print("InfluxDB connection established")

        value = self.apolo.classify_request(
            list_load_request=last_element, url="/app/apolo/saved_apolo/Apolo"
        )

        element = last_element[0].decode("utf-8")
        element_obj = json.loads(element)
        self.ixs.add_influxdb_data(
            influxdb_connection=influxdb_connection,
            bucket="requests_scores",
            measurement_name="weblogs",
            value=value,
            tags=element_obj,
        )

        print(
            "Last element of the Redis list added to the InfluxDB database, with value: "
            + str(value)
        )

        # Close the InfluxDB connection
        self.ixs.close_influxdb_connection(influxdb_connection=influxdb_connection)

        print("InfluxDB connection closed")

    def get_dataset(self, url: str) -> None:
        # TODO: Change this method to get the dataset from the InfluxDB database
        print("Getting dataset from url: " + url)
        self.dataset = pd.read_csv(url)
