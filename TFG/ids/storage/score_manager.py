# ========================== ScoreManager ==========================
#
#                   Author:  Sergio Arroni Del Riego
#
# ================================================================

# ==================> Imports
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
        apolo (object): ApoloPredict object

    """

    def __init__(self) -> None:
        """__init__

        This method is used to initialize the ScoreManager class.

        Parameters:

        Output:
            None
        """
        self.ixs: InfluxDBService = InfluxDBService()
        self.apolo_predict: ApoloPredict = ApoloPredict()

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

        value, arms = self.apolo_predict.classify_request(
            list_load_request=last_element, url="/app/apolo/saved_apolo/Apolo"
        )
        value = value[0]
        arms = arms[0]
        print("Value: " + str(value))
        print("Arms: " + str(arms))

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
            f"Last element of the Redis list added to the InfluxDB database, with value: {str(value)} and arms: {str(arms)}"
        )

        # Close the InfluxDB connection
        self.ixs.close_influxdb_connection(influxdb_connection=influxdb_connection)

        print("InfluxDB connection closed")
