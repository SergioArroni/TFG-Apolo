# ========================== MLP =========================
#
#                   Author:  Sergio Arroni Del Riego
#
# =============================================================================

# ==================> Imports
from apolo.layers.models import Model

from sklearn.neural_network import MLPClassifier


# ==================> Classes
class MLP(Model):
    """MLP

    This class is used to create a MLP model.

    Parameters:
        x_train: Training data
        y_train: Training labels
        x_test: Test data
        y_test: Test labels
        dataset: Dataset name
        exe: Execute the model or not
    Output:
        None
    """

    def __init__(
        self,
        seed: int,
        x_train: list = None,
        y_train: list = None,
        x_test: list = None,
        y_test: list = None,
        dataset: str = None,
        exe: bool = False,
    ) -> None:
        """__init__

        This method is used to initialize the MLP class.

        Parameters:
            x_train: Training data
            y_train: Training labels
            x_test: Test data
            y_test: Test labels
            dataset: Dataset name
        Output:
            None
        """
        super().__init__(x_train, y_train, x_test, y_test, dataset, seed=seed)
        if exe:
            self.exe()

    # Override
    def expecific_model(self) -> object:
        """expecific_model

        This method is an override of the parent method for the case of the MLP model.

        Output:
            object: MLP model
        """
        mlp = MLPClassifier(
            hidden_layer_sizes=(32, 32, 32),
            max_iter=200,
            verbose=False,
            random_state=self.seed,
            batch_size=200,
            early_stopping=True,
            activation="relu",
            solver="adam",
        )
        return mlp

    # Override
    def __str__(self) -> str:
        """__str__

        This method is used to return the name of the class.

        Output:
            str: Name of the class
        """
        return self.__class__.__name__
