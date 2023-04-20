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
import os

# Main function
def main() -> None:
    """
    Main function of the project.
    """
    # Example of how to get the last N elements of a Redis list and add them to an InfluxDB database with
    # auto score calculation.

    # Get a Redis connection
    redis_connection = get_redis_connection(host="redis", port=6379, db=0)
    print("Redis connection established")
    # Get the last element of the Redis list and delete it from the list
    last_element = get_redis_list_last_n_elements_and_delete_them(redis_connection=redis_connection,
                                                                  list_name="gatewaylogs", n=1)
    print("Last element of the Redis list: " + str(last_element))
    # Close the Redis connection
    close_redis_connection(redis_connection=redis_connection)
    print("Redis connection closed")
    # Get an InfluxDB connection
    influxdb_connection = get_influxdb_connection(
        url="http://influxdb:8086", token=os.environ.get('INFLUXDB_TOKEN'), org="TFG")
    # Add the last element of the Redis list to the InfluxDB database
    print("InfluxDB connection established")
    random_value = randint(0, 100)
    element = last_element[0].decode("utf-8")
    element_obj = json.loads(element)
    add_influxdb_data(
        influxdb_connection=influxdb_connection,
        bucket="requests_scores",
        measurement_name="weblogs",
        value=random_value,
        tags=element_obj
    )
    print("Last element of the Redis list added to the InfluxDB database, with value: " + str(random_value))
    # Close the InfluxDB connection
    close_influxdb_connection(influxdb_connection=influxdb_connection)
    print("InfluxDB connection closed")

# Main function call
if __name__ == "__main__":
    main()
