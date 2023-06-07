# ========================== Decision Tree Classifier =========================
#
#                   Author:  Sergio Arroni Del Riego
#
# =============================================================================

# ==================> Imports
from apolo.layers.models import Model

from sklearn.tree import DecisionTreeClassifier


# ==================> Classes
class DecisionTree(Model):
    def __init__(
        self,
        seed: int,
        x_train: list = None,
        y_train: list = None,
        x_test: list = None,
        y_test: list = None,
        dataset: str = None,
        exe: bool = True,
    ) -> None:
        """__init__

        This method is used to initialize the DecisionTree class.

        Parameters:
            x_train: Training data
            y_train: Training labels
            x_test: Test data
            y_test: Test labels
            dataset: Dataset name
        Output:
            None
        """
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
    def expecific_model(self) -> DecisionTreeClassifier:
        """expecific_model

        This method is an override of the parent method for the case of the DecisionTree model.

        Output:
            DecisionTreeClassifier
        """
        return DecisionTreeClassifier()

    # Override
    def __str__(self) -> str:
        """__str__

        This method is used to return the name of the class.

        Output:
            str: Name of the class
        """
        return self.__class__.__name__
