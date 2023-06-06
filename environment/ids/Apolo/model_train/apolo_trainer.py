# ========================== ApoloTrainer ==========================
#
#                   Author:  Sergio Arroni Del Riego
#
# ================================================================

# ==================> Imports
import pandas as pd

# ==================> Classes
class ApoloTrainer:
    def __init__(self) -> None:
        """__init__

        This method is used to initialize the ApoloTrainer class.

        Parameters:

        Output:
            None
        """
        pass

    def train_model(
        self, model: object, dataset: pd.DataFrame, url: str = "../saved_models/Apolo"
    ) -> None:
        """train_model

        This method is used to train a model.

        Parameters:
            model: Model to train.
            dataset: Dataset to use for training.
            url: URL where the model will be saved.
        Output:
            None
        """
        pass

    def test_model(self, dataset: pd.DataFrame, url: str = "../saved_apolo/Apolo") -> None:
        """test_model

        This method is used to test a model.

        Parameters:
            dataset: Dataset to use for testing.
            url: URL where the model is saved.
        Output:
            None
        """
        pass
