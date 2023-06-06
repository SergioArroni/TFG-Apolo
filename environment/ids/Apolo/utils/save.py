# ========================== Save Data & Models Utils ==========================
#
#                   Author:  Sergio Arroni Del Riego
#
# ==============================================================================

# ==================> Imports
import pickle
import pandas as pd


class UtilsSave:
    def __init__(self, seed: int = 42):
        """__init__

        This method is used to initialize the Utils class.

        Parameters:
            seed (int): seed for reproducibility
        Output:
            None
        """
        self.seed = seed
        pass

    def save_model(self, model, name: str) -> None:
        """save_model

        This function saves the model

        Parameters:
            model: model to save
            name (str): name of the model
        Output:
            None
        """
        # Its important to use binary mode
        name = f"intrusion_detection_systems/models/saved_models/{name}"
        save = open(name, "wb")

        # source, destination
        pickle.dump(model, save)

        # close the file
        save.close()

    def save_data(self, df: pd.DataFrame, name: str) -> None:
        """save_data

        This function saves the data

        Parameters:
            df (pd.DataFrame): dataframe to save
            name (str): name of the dataframe
        Output:
            None
        """
        df.to_csv(f"./data_prep/merged/{name}.csv", index=False)
