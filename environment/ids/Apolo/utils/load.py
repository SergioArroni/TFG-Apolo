# ========================== Load Data & Models Utils ==========================
#
#                   Author:  Sergio Arroni Del Riego
#
# ==============================================================================

# ==================> Imports
import pandas as pd
import pickle
from preprocesing import preprocess_dataset


class UtilsLoad:
    def __init__(self, seed: int = 42) -> None:
        """__init__

        This method is used to initialize the Utils class.

        Parameters:

        Output:
            None
        """
        self.seed = seed
        self.list_load_dataset = [
            "./shared/data/CIC_2017/Thursday-WorkingHours-Afternoon-Infilteration.pcap_ISCX.csv",
            "./shared/data/CIC_2017/Thursday-WorkingHours-Morning-WebAttacks.pcap_ISCX.csv",
            "./shared/data/CIC_2017/Tuesday-WorkingHours.pcap_ISCX.csv",
        ]

    # ==================> Functions
    def load_data(self, path: list, seed: int) -> pd.DataFrame:
        """load_data

        This function loads the data from the path and returns a dataframe of the datasets

        Parameters:
            path (list): list of paths to the files
        Output:
            df (pd.DataFrame): dataframe with all the data
        """
        i = 0
        df = pd.read_csv(path[i])
        while True:
            i += 1
            if i == len(path):
                break
            df = pd.concat([df, pd.read_csv(path[i])])
        return df.sample(frac=1, random_state=seed)

    def load_model(self, name: str) -> object:
        # load the model from disk
        return pickle.load(open(name, "rb"))

    # TODO

    def load_dataset(
        self,
        dataset_type: str,
        name: str = "CIC-IDS_2017_MAB",
        load_dataset: bool = False,
        save: bool = True,
    ) -> object:
        """load_dataset

        This method is used to load the dataset.

        Parameters:
            dataset_type: Type of dataset
            name: Name of the dataset
            load_dataset: If True, the dataset will be loaded from the path
            save: If True, the dataset will be saved in the path
        Output:
            None
        """
        if not load_dataset:
            # Preprocesar el dataset
            df = self.load_data(
                self.list_load_dataset,
                self.seed,
            )

            print("Dataset cargado")

            df_preprocessed = preprocess_dataset(
                df,
                save=save,
                dataset_type=dataset_type,
                seed=self.seed,
                load=load_dataset,
                name_save=name,
                name_load=name,
            )
        else:
            df_preprocessed = preprocess_dataset(
                pd.DataFrame(),
                save=save,
                dataset_type=dataset_type,
                seed=self.seed,
                load=load_dataset,
                name_save=name,
                name_load=name,
            )

        print("Dataset Preprocesado")
        return df_preprocessed
