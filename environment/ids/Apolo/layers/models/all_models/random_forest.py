# ========================== Random Forest Classifier =========================
#
#                   Author:  Sergio Arroni Del Riego
#
# =============================================================================

# ==================> Imports
from apolo.layers.models import Model

from sklearn.ensemble import RandomForestClassifier


# ==================> Classes
class RandomForest(Model):
    def __init__(
        self,
        seed: int,
        x_train: list = None,
        y_train: list = None,
        x_test: list = None,
        y_test: list = None,
        dataset: str = None,
        n_estimators: int = 100,
        n_jobs: int = -1,
        exe: bool = True,
    ) -> None:
        """__init__

        This method is used to initialize the RandomForest class.

        Parameters:
            x_train: Training data
            y_train: Training labels
            x_test: Test data
            y_test: Test labels
            dataset: Dataset name
            n_estimators: Number of estimators
            n_jobs: Number of jobs
        Output:
            None
        """
        self.n_estimators = n_estimators
        self.n_jobs = n_jobs
        if exe:
            super().__init__(
                x_train=x_train,
                y_train=y_train,
                x_test=x_test,
                y_test=y_test,
                dataset=dataset,
                seed=seed,
            )
            self.exe()

    # Override
    def expecific_model(self) -> RandomForestClassifier:
        """expecific_model

        This method is an override of the parent method for the case of the RandomForest model.

        Output:
            object: RandomForest model
        """
        return RandomForestClassifier(
            n_estimators=self.n_estimators, n_jobs=self.n_jobs, random_state=self.seed
        )

    # Override
    def __str__(self) -> str:
        """__str__

        This method is used to return the name of the class.

        Output:
            str: Name of the class
        """
        return f"{self.__class__.__name__}, n_estimations: {self.n_estimators}, n_jobs: {self.n_jobs}"
