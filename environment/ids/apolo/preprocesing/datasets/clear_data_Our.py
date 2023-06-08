# ========================== Clear Data - DATE ==========================
#
#                   Author:  Sergio Arroni Del Riego
#
# ===============================================================================

# ==================> Imports

import pandas as pd
from apolo.preprocesing import ClearData


# ==================> Functions
class ClearDataOur(ClearData):
    """ClearDataOur

    This class is used to clear the data from our architecture.

    """

    def __init__(
        self, df: pd.DataFrame, do_save: bool, seed: int, name_save: str, name_load: str
    ) -> None:
        """__init__

        This method is used to initialize the ClearDataOur class.

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

        This method is used to clear the data from our architecture.

        Output:
            None
        """
        
        self.drop_duplicate_columns()

        self.drop_bad_elements()
        
        print("dddddddddddddddddd")

        print(self.df.head())
        print(self.df.columns)

        print("----------------------------------------------------------------")
        
        print(self.df.columns)


        self.x = self.df.drop(["Label"], axis=1)
        self.y = self.df["Label"]

        labels = set(self.y)

        labels.remove("No Label")

        print(f"labels: {labels}")

        self.drop_bad_elements_x()

            
        print(self.x)
        if self.do_save:
            self.save_data()

    # Override
    def save_data(self):
        aux_df = self.df
        aux_df.drop([" Label"], axis=1, inplace=True)
        
        if self.y is not None:
            aux_y = pd.DataFrame(self.y, columns=[" Label"])
            aux_y.to_csv(f"apolo/preprocesing/data/save/data_our/{self.name_save}_y.csv", index=False)
            
        aux_df = pd.concat([aux_df, aux_y], axis=1)

        aux_df.to_csv(f"apolo/preprocesing/data/save/data_our/{self.name_save}.csv", index=False)