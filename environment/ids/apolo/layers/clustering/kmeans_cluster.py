# ========================== KMeans =========================
#
#                   Author:  Sergio Arroni Del Riego
#
# =============================================================================

# ==================> Imports
from sklearn.cluster import KMeans
from apolo.layers.models import Model


# ==================> Classes
class KMeansCluster(Model):
    """KMeansCluster

    This class is used to create a KMeans model.

    Attributes:
        k: Number of clusters
    """

    def __init__(
        self,
        seed: int,
        x_train: list = None,
        y_train: list = None,
        x_test: list = None,
        y_test: list = None,
        dataset: str = None,
        k: int = 2,
        exe: bool = False,
    ) -> None:
        """__init__

        This method is used to initialize the KMeans class.

        Parameters:
            x_train: Training data
            y_train: Training labels
            x_test: Test data
            y_test: Test labels
            dataset: Dataset name
            k: Number of clusters
        Output:
            None
        """
        self.k = k
        super().__init__(
            x_train=x_train,
            y_train=y_train,
            x_test=x_test,
            y_test=y_test,
            dataset=dataset,
            seed=seed,
        )
        if exe:
            self.exe()

    # Override
    def expecific_model(self) -> KMeans:
        """expecific_model

        This method is an override of the parent method for the case of the KNeighbors model.

        Output:
            KNeighborsClassifier
        """

        return KMeans(n_clusters=self.k, random_state=self.seed)

    # Override
    def __str__(self) -> str:
        """__str__

        This method is used to return the name of the class.

        Output:
            str: Name of the class
        """
        return f"{self.__class__.__name__}({self.k})"
