# ====================== Adversarial Machine Learning Protected Intrusion Detection System ======================
#
# Main file of the Adversarial Machine Learning Protected Intrusion Detection System (IDS) project.
# This file contains the main function of the project.
#
# Author: Sergio Arroni Del Riego
#
# ================================================================================================================


# Imports
from storage import DataCollector, ScoreManager
import time


# Main function
def main() -> None:
    """
    Main function of the project.
    """
    # Example of how to get the last N elements of a Redis list and add them to an InfluxDB database with
    # auto score calculation.
    dc = DataCollector()
    sm = ScoreManager()
    

    while True:
        redis_connection = dc.redis.get_redis_connection(
            host="redis", port=6379, db=0
        )
        print("Redis connection established")
        list_name="gatewaylogs"
        
        lista = dc.redis.get_redis_list(redis_connection=redis_connection, list_name=list_name)
        while len(lista) > 0:
            dc.get_data_from_queue(list_name=list_name, redis_connection=redis_connection)

            sm.push_data_to_influxdb(
                last_element=dc.last_element, url="http://influxdb:8086", org="TFG"
            )

            lista = dc.redis.get_redis_list(redis_connection=redis_connection, list_name=list_name)
        time.sleep(5)
        
        # Close the Redis connection
        dc.redis.close_redis_connection(redis_connection=redis_connection)
        print("Redis connection closed")



# Main function call
if __name__ == "__main__":
    main()
