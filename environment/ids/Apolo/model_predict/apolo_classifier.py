# ========================== ApoloPredict ==========================
#
#                   Author:  Sergio Arroni Del Riego
#
# ================================================================

# ==================> Imports
from utils import UtilsLoad


# ==================> Classes
class ApoloPredict:
    def __init__(self) -> None:
        """__init__

        This method is used to initialize the ApoloPredict class.

        Parameters:

        Output:
            None
        """

    def classify_request(
        self, request: object, url: str = "../saved_apolo/Apolo"
    ) -> int:
        """classify_request

        This method is used to classify a request.

        Parameters:
            request: Request to classify.
            url: URL where the model is saved.
        Output:
            Classification result.
        """
        ul = UtilsLoad()
        
        return ul.load_model(name = url).predict(request)
