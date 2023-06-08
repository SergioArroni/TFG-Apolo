# ========================== ApoloPredict ==========================
#
#                   Author:  Sergio Arroni Del Riego
#
# ================================================================

# ==================> Imports
from utils import UtilsLoad
from utils import DataSelector


# ==================> Classes
class ApoloPredict:
    """ApoloPredict

    This class is used to predict a request.

    Attributes:
        ul: UtilsLoad object.
    """

    def __init__(self, seed: int = 42) -> None:
        """__init__

        This method is used to initialize the ApoloPredict class.

        Parameters:

        Output:
            None
        """
        self.seed = seed
        self.ul = UtilsLoad()
        self.data_prep = DataSelector(seed=self.seed)

    def classify_request(
        self, list_load_request: list, url: str = "apolo/saved_apolo/Apolo"
    ) -> tuple:
        """classify_request

        This method is used to classify a request.

        Parameters:
            list_load_request: List of paths to load the request.
            url: URL where the model is saved.
        Output:
            Classification result.
        """
        df_preprocessed = self.data_prep.load_request(
            dataset_type="Data_Our", list_load_request=list_load_request
        )

        y_pred, arms = self.ul.load_model(name=url).predict(df_preprocessed.x)

        return y_pred, arms
