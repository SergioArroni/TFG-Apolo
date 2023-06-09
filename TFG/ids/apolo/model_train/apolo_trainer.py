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

    def __init__(self, seed: int = 42) -> None:
        """__init__

        This method is used to initialize the ApoloTrainer class.

        Parameters:

        Output:
            None
        """
        self.us: UtilsSave = UtilsSave()
        self.ul: UtilsLoad = UtilsLoad()
        self.seed = seed
        arms = [
            RandomForest(seed=self.seed, exe=False).expecific_model(),
            DecisionTree(seed=self.seed, exe=False).expecific_model(),
            NaiveBayes(seed=self.seed, exe=False).expecific_model(),
            LogisticRegressionModel(seed=self.seed, exe=False).expecific_model(),
            MLP(seed=self.seed, exe=False).expecific_model(),
        ]
        self.mab = MAB(arms=arms, n_clusters=2)

    def train_model(
        self,
        X_train: list,
        y_train: list,
        X_test: list,
        y_test: list,
        url: str = "apolo/saved_apolo/Apolo",
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

        self.mab.train(X_test=X_test, y_test=y_test, X_train=X_train, y_train=y_train)
        self.us.save_model(self.mab, url)

    def test_model(
        self, df_preprocessed: object, url: str = "apolo/saved_apolo/Apolo"
    ) -> None:
        """test_model

        This method is used to test a model.

        Parameters:
            df_preprocessed: Preprocessed dataset.
            url: URL where the model is saved.
        Output:
            None
        """

        model = self.ul.load_model(name=url)
        model.test(df_preprocessed)
        print("Tested")
        model.print_arms_test()
        print("Printed")
