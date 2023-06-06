# ========================== ScoreManager ==========================
#
#                   Author:  Sergio Arroni Del Riego
#
# ================================================================

# ==================> Imports
import pandas as pd
import os
import json
from random import randint
from services import influxdb_service as ixs

# ==================> Classes
class ScoreManager:
    def __init__(self) -> None:
        """__init__

        This method is used to initialize the ScoreManager class.

        Parameters:

        Output:
            None
        """
        pass

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
        influxdb_connection = ixs.get_influxdb_connection(
            url=url,
            token=os.environ.get("INFLUXDB_TOKEN"),
            org=org,
        )
        # Add the last element of the Redis list to the InfluxDB database
        print("InfluxDB connection established")
        
        random_value = randint(0, 100)
        element = last_element[0].decode("utf-8")
        element_obj = json.loads(element)
        ixs.add_influxdb_data(
            influxdb_connection=influxdb_connection,
            bucket="requests_scores",
            measurement_name="weblogs",
            value=random_value,
            tags=element_obj,
        )
        
        print(
            "Last element of the Redis list added to the InfluxDB database, with value: "
            + str(random_value)
        )
        
        # Close the InfluxDB connection
        ixs.close_influxdb_connection(influxdb_connection=influxdb_connection)
        
        print("InfluxDB connection closed")

    def get_dataset(self, url: str) -> None:
        #TODO: Change this method to get the dataset from the InfluxDB database
        print("Getting dataset from url: " + url)
        self.dataset = pd.read_csv(url)
