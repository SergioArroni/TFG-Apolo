# ========================== Clear Data - CIC IDS 2017 ==========================
#
#                   Author:  Sergio Arroni Del Riego
#
# ===============================================================================

# ==================> Imports

import pandas as pd
from apolo.preprocesing import ClearData


# ==================> Functions
class ClearDataCIC2017(ClearData):
    """ClearDataCIC2017

    This class is used to clear the data of the CIC 2017 dataset.

    Attributes:
        df: pd.DataFrame
        do_save: bool
        name_save: str
        name_load: str
    """

    def __init__(
        self, df: pd.DataFrame, do_save: bool, seed: int, name_save: str, name_load: str
    ) -> None:
        """__init__

        This method is used to initialize the ClearDataCIC2017 class.

        Parameters:
            df: pd.DataFrame
            do_save: bool
        Output:
            None
        """
        super().__init__(df=df, seed=seed)
        self.do_save = do_save
        self.name_save = name_save
        self.name_load = name_load

    # Override
    def clear_data(self) -> None:
        """clear_data

        This method is used to clear the data of the CIC 2017 dataset.

        Output:
            None
        """
        # self.best_features_func()
        self.drop_one_features()
        self.drop_duplicate_columns()

        self.drop_bad_elements()
        self.x = self.df.drop([" Label"], axis=1)
        self.y = self.df[" Label"]

        labels = set(self.y)

        labels.remove("BENIGN")

        print(f"labels: {labels}")

        self.replace(list_B_columns=["BENIGN"], list_M_columns=labels)

        self.drop_bad_elements_x()

        if self.do_save:
            self.save_data()

    # Override
    def save_data(self) -> None:
        aux_df = self.df
        aux_df.drop([" Label"], axis=1, inplace=True)

        aux_y = pd.DataFrame(self.y, columns=[" Label"])
        aux_df = pd.concat([aux_df, aux_y], axis=1)

        aux_df.to_csv(f"./shared/data_prep/CIC17/{self.name_save}.csv", index=False)

        aux_y.to_csv(f"./shared/data_prep/CIC17/{self.name_save}_y.csv", index=False)

    # Override
    def load_data(self) -> tuple:
        df = pd.read_csv(f"./shared/data_prep/CIC17/{self.name_load}.csv")
        y = pd.read_csv(f"./shared/data_prep/CIC17/{self.name_load}_y.csv")
        return df, y
