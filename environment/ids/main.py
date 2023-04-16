# ====================== Adversarial Machine Learning Protected Intrusion Detection System ======================
#
# Main file of the Adversarial Machine Learning Protected Intrusion Detection System (IDS) project.
# This file contains the main function of the project.
#
# Author: Sergio Arroni Del Riego
#
# ================================================================================================================


# Imports
import json
from random import randint
from services.influxdb_service import *
from services.redis_service import *


# Main function
def main() -> None:
    """
    Main function of the project.
    """
    # Example of how to get the last N elements of a Redis list and add them to an InfluxDB database with
    # auto score calculation.

    # Get a Redis connection
    redis_connection = get_redis_connection(host="localhost", port=6379, db=0)
    # Get the last element of the Redis list and delete it from the list
    last_element = get_redis_list_last_n_elements_and_delete_them(redis_connection=redis_connection,
                                                                  list_name="weblogs", n=1)
    # Close the Redis connection
    close_redis_connection(redis_connection=redis_connection)

    # Get an InfluxDB connection
    token = "FT84qZnEg4Ef_jd_sSRJVBy6PMkbfJLakGeeTZouJqmZMI4DI6k6i3n0YNExmSwlhSI0vNB-MZH16zmEzRClqg=="
    influxdb_connection = get_influxdb_connection(url="http://localhost:8086", token=token, org="uniovi")
    # Add the last element of the Redis list to the InfluxDB database
    random_value = randint(0, 100)
    element = last_element[0].decode("utf-8")
    element_obj = json.loads(element)
    add_influxdb_data(
        influxdb_connection=influxdb_connection,
        bucket="requests_scores",
        measurement_name="weblogs",
        value=float(85),
        tags=element_obj
    )
    # Close the InfluxDB connection
    close_influxdb_connection(influxdb_connection=influxdb_connection)


# Main function call
if __name__ == "__main__":
    main()
