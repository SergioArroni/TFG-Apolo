# ========================== ApoloPredict ==========================
#
#                   Author:  Sergio Arroni Del Riego
#
# ================================================================

# ==================> Imports
from utils import UtilsLoad
from utils import DataPreprocessing


# ==================> Classes
class ApoloPredict:
    """ApoloPredict

    This class is used to predict a request.

    Attributes:
        ul: UtilsLoad object.
    """

    def __init__(self, seed:int = 42) -> None:
        """__init__

        This method is used to initialize the ApoloPredict class.

        Parameters:

        Output:
            None
        """
        self.seed = seed
        self.ul = UtilsLoad()
        self.data_prep = DataPreprocessing(seed=self.seed)

    def classify_request(
        self, nombre_dataset: str, request: list, url: str = "../saved_apolo/Apolo"
    ) -> int:
        """classify_request

        This method is used to classify a request.

        Parameters:
            request: Request to classify.
            url: URL where the model is saved.
        Output:
            Classification result.
        """
        df_preprocessed = self.data_prep.load_request(dataset_type="Data_Our")

        return self.ul.load_model(name=url).predict(df_preprocessed.df)
