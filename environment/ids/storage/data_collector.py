# ========================== DataCollector ==========================
#
#                   Author:  Sergio Arroni Del Riego
#
# ================================================================

# ==================> Imports
import pandas as pd
from services import RedisService


# ==================> Classes
class DataCollector:
    """DataCollector

    This class is used to collect the data from the Redis queue.

    Attributes:
        redis (object): RedisService object
        last_element (list): Last element of the Redis list.
        dataset (object): Dataset.
    """

    def __init__(self) -> None:
        """__init__

        This method is used to initialize the DataCollector class.

        Parameters:

        Output:
            None
        """
        self.redis: RedisService = RedisService()
        self.last_element = []

    def get_data_from_queue(
        self, redis_connection, list_name: str = "gatewaylogs"
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

        # Get the last element of the Redis list and delete it from the list
        self.last_element = self.redis.get_redis_list_last_n_elements_and_delete_them(
            redis_connection=redis_connection, list_name=list_name, n=1
        )

        print("Last element of the Redis list: " + str(self.last_element))
