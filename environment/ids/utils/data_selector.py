# ========================== Data Preprocessing ==========================
#
#                   Author:  Sergio Arroni Del Riego
#
# ======================================================================

# ==================> Imports
import pandas as pd
import json
from utils import UtilsLoad
from apolo.preprocesing import (
    ClearData,
    CIC_2017,
    CIC_2018,
    CIC_2019,
    Data_Our,
    transform,
)

# ===================> Enumerations
datasets_types = {
    "CIC_2017": CIC_2017,
    "CIC_2018": CIC_2018,
    "CIC_2019": CIC_2019,
    "Data_Our": Data_Our,
}


# ==================> Functions
class DataSelector:
    """DataPreprocessing

    This class is used to preprocess the data.

    Attributes:
        seed: Seed for the random state
        usl: UtilsLoad object
        list_load_dataset: List of paths to load the dataset
    """

    def __init__(self, seed: int = 42) -> None:
        """__init__

        This method is used to initialize the DataPreprocessing class.

        Parameters:
            seed: Seed for the random state
        Output:
            None
        """
        self.seed = seed
        self.usl = UtilsLoad()
        self.list_load_dataset = [
            "apolo/preprocesing/data/CIC_2017/Thursday-WorkingHours-Afternoon-Infilteration.pcap_ISCX.csv",
            "apolo/preprocesing/data/CIC_2017/Thursday-WorkingHours-Morning-WebAttacks.pcap_ISCX.csv",
            "apolo/preprocesing/data/CIC_2017/Tuesday-WorkingHours.pcap_ISCX.csv",
        ]

    def load_dataset(
        self,
        dataset_type: str,
        name: str = None,
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
            df = self.usl.load_data(
                self.list_load_dataset,
                self.seed,
            )

            print("Dataset cargado")

            df_preprocessed = self.preprocess_dataset(
                df,
                save=save,
                dataset_type=dataset_type,
                seed=self.seed,
                load=load_dataset,
                name_save=name,
                name_load=name,
            )
        else:
            df_preprocessed = self.preprocess_dataset(
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

    def preprocess_dataset(
        self,
        df: pd.DataFrame,
        save: bool,
        dataset_type: str,
        seed: int,
        name_save: str,
        name_load: str,
        load: bool = True,
    ) -> transform:
        """preprocess_dataset

        This function preprocesses a dataset

        Parameters:
            df: Dataframe to preprocess
            save: Save the dataset
            dataset_type: Type of dataset
        Output:
            Transform object
        """
        data: ClearData = datasets_types[dataset_type](
            df=df, do_save=save, seed=seed, name_save=name_save, name_load=name_load
        )
        if load:
            print("Loading existing data")
            x, y = data.load_data()
            trans = transform(x=x, y=y, size=0.3, seed=seed)
        else:
            print("Loading new data")
            data.clear_data()
            trans = transform(x=data.x, y=data.y, size=0.3, seed=seed)
        trans.transform()
        return trans

    def preprocess_request(
        self,
        df: pd.DataFrame,
        save: bool,
        dataset_type: str,
        seed: int,
        name_save: str,
        name_load: str,
    ) -> transform:
        """preprocess_request

        This function preprocesses a request

        Parameters:
            df: Dataframe to preprocess
            save: Save the dataset
            dataset_type: Type of dataset
        Output:
            Transform object
        """
        
        print("bbb")

        print(df.head())
        print(df.columns)

        data: ClearData = datasets_types[dataset_type](
            df=df, do_save=save, seed=seed, name_save=name_save, name_load=name_load
        )
        
        print("ccc")

        print(df.head())
        print(df.columns)


        print("Loading new data")
        data.clear_data()
        trans = transform(x=data.x, y=data.y, seed=seed, df=data.df)

        trans.transform_request()
        return trans

    def load_request(
        self,
        dataset_type: str,
        list_load_request: list,
        name: str = None,
        save: bool = False,
    ) -> object:
        """load_request

        This method is used to load the request.

        Parameters:
            dataset_type: Type of dataset
            name: Name of the dataset
            save: If True, the dataset will be saved in the path
        Output:
            object
        """

        list_load_request = json.loads([l.decode("utf-8") for l in list_load_request][0])

        # Preprocesar el dataset
        df = self.usl.load_data(
            seed=self.seed,
            json=list_load_request,
        )
        print("AQUII")

        print(df.head())
        print(df.columns)

        print("Dataset cargado")

        df_preprocessed = self.preprocess_request(
            df=df,
            save=save,
            dataset_type=dataset_type,
            seed=self.seed,
            name_save=name,
            name_load=name,
        )

        print("Dataset Preprocesado")
        return df_preprocessed
