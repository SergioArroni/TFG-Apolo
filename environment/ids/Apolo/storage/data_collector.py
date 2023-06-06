# ========================== DataCollector ==========================
#
#                   Author:  Sergio Arroni Del Riego
#
# ================================================================

# ==================> Imports
import pandas as pd
from services import redis_service as rs


# ==================> Classes
class DataCollector:
    def __init__(self) -> None:
        """__init__

        This method is used to initialize the DataCollector class.

        Parameters:

        Output:
            None
        """
        pass

    def get_data_from_queue(
        self, redis_db: int, redis_port: int = 6379, list_name: str = "gatewaylogs"
    ) -> None:
        """get_data_from_queue

        This method is used to get the data from the Redis queue.

        Parameters:
            redis_db: Redis database.
            redis_port: Redis port.
            list_name: Redis list name.
        Output:
            None
        """

        redis_connection = rs.get_redis_connection(
            host="redis", port=redis_port, db=redis_db
        )

        print("Redis connection established")

        # Get the last element of the Redis list and delete it from the list
        self.last_element = rs.get_redis_list_last_n_elements_and_delete_them(
            redis_connection=redis_connection, list_name=list_name, n=1
        )

        print("Last element of the Redis list: " + str(self.last_element))

        # Close the Redis connection
        rs.close_redis_connection(redis_connection=redis_connection)

        print("Redis connection closed")

    def get_dataset(self, url: str) -> None:
        #TODO
        print("Getting dataset from url: " + url)
        self.dataset = pd.read_csv(url)
