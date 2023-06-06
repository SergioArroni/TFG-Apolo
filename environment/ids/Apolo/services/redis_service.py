# ====================== Adversarial Machine Learning Protected Intrusion Detection System ======================
#
# Redis service -> Functions to get the last N elements of a Redis list, and remove them from the list.
#
# Author: Sergio Arroni Del Riego
#
# ================================================================================================================

# Imports
import redis


class RedisService:
    def __init__(self) -> None:
        """
        Initialize the RedisService class.

        Parameters:
            None
        Output:
            None
        """
        pass

    # Functions
    def get_redis_connection(self, host: str, port: int, db: int) -> redis.Redis:
        """
        Get a Redis connection instance.

        Args:
            host: Redis host.
            port: Redis port.
            db: Redis database.
        Returns:
            Redis connection instance.
        """
        return redis.Redis(host=host, port=port, db=db)

    def close_redis_connection(self, redis_connection: redis.Redis) -> None:
        """
        Close a Redis connection.

        Args:
            redis_connection: Redis connection.
        Returns:
            None.
        """
        redis_connection.close()

    def get_redis_list(self, redis_connection: redis.Redis, list_name: str) -> list:
        """
        Get a Redis list.

        Args:
            redis_connection: Redis connection.
            list_name: Redis list name.
        Returns:
            Redis list.
        """
        return redis_connection.lrange(list_name, start=0, end=-1)

    def get_redis_list_last_n_elements(
        self, redis_connection: redis.Redis, list_name: str, n: int
    ) -> list:
        """
        Get the last N elements of a Redis list.

        Args:
            redis_connection: Redis connection.
            list_name: Redis list name.
            n: Number of elements to get.
        Returns:
            Last N elements of the Redis list.
        """
        return redis_connection.lrange(list_name, start=-n, end=-1)

    def get_redis_list_last_n_elements_and_delete_them(
        self, redis_connection: redis.Redis, list_name: str, n: int
    ) -> list:
        """
        Get the last N elements of a Redis list and remove them from the list.

        Args:
            redis_connection: Redis connection.
            list_name: Redis list name.
            n: Number of elements to get and remove.
        Returns:
            Last N elements of the Redis list.
        """
        elements = self.get_redis_list_last_n_elements(
            self, redis_connection=redis_connection, list_name=list_name, n=n
        )
        self.remove_redis_list_last_n_elements(
            redis_connection=redis_connection, list_name=list_name, n=n
        )
        return elements

    def remove_redis_list_last_n_elements(
        self, redis_connection: redis.Redis, list_name: str, n: int
    ) -> None:
        """
        Remove the last N elements of a Redis list.

        Args:
            redis_connection: Redis connection.
            list_name: Redis list name.
            n: Number of elements to remove.
        Returns:
            None.
        """
        redis_connection.ltrim(list_name, start=0, end=-n - 1)

    def remove_redis_list_all_elements(
        self, redis_connection: redis.Redis, list_name: str
    ) -> None:
        """
        Remove all elements of a Redis list.

        Args:
            redis_connection: Redis connection.
            list_name: Redis list name.
        Returns:
            None.
        """
        redis_connection.delete(list_name)
