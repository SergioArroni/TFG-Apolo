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
from Apolo.storage import DataCollector, ScoreManager
from Apolo.services import RedisService as rs
import os
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
        lista = rs.get_redis_list()
        while len(lista) > 0:
            dc.get_data_from_queue(redis_db=0, redis_port=6379, list_name="gatewaylogs")

            sm.push_data_to_influxdb(
                last_element=dc.last_element, url="http://influxdb:8086", org="TFG"
            )

            lista = rs.get_redis_list()
        time.sleep(5)


# Main function call
if __name__ == "__main__":
    main()
