# ========================== ApoloTrainer ==========================
#
#                   Author:  Sergio Arroni Del Riego
#
# ================================================================

# ==================> Imports
from apolo.layers import MAB
from utils import UtilsSave, UtilsLoad
from apolo.layers.models import (
    RandomForest,
    DecisionTree,
    NaiveBayes,
    LogisticRegressionModel,
    MLP,
)


# ==================> Classes
class ApoloTrainer:
    """ApoloTrainer

    This class is used to train a model.

    Attributes:
        us: UtilsSave object.
        ul: UtilsLoad object.
    """

    def __init__(self) -> None:
        """__init__

        This method is used to initialize the ApoloTrainer class.

        Parameters:

        Output:
            None
        """
        self.us = UtilsSave()
        self.ul = UtilsLoad()
        arms = [
            RandomForest(seed=seed, exe=False),
            DecisionTree(seed=seed, exe=False),
            NaiveBayes(seed=seed, exe=False),
            LogisticRegressionModel(seed=seed, exe=False),
            MLP(seed=seed, exe=False),
        ]
        self.mab = MAB()

    def train_model(
        self,
        X_train: list,
        y_train: list,
        X_test: list,
        y_test: list,
        url: str = "../saved_models/Apolo",
    ) -> None:
        """train_model

        This method is used to train a model.

        Parameters:
            X_train: Training data.
            y_train: Training labels.
            X_test: Testing data.
            y_test: Testing labels.
            url: URL where the model will be saved.
        Output:
            None
        """

        model = self.mab.train(X_train, y_train, X_test, y_test)
        self.us.save_model(model, url)

    def test_model(self, X_test: list, url: str = "../saved_apolo/Apolo") -> None:
        """test_model

        This method is used to test a model.

        Parameters:
            X_test: Testing data.
            url: URL where the model is saved.
        Output:
            None
        """

        UtilsLoad.load_model(url).test(X_test)
