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
        
        print(self.df.columns)
        if "Flow ID" in self.df.columns:
            self.df.drop(["Flow ID"], axis=1, inplace=True)
            
        if "Src IP" in self.df.columns:
            self.df.drop(["Src IP"], axis=1, inplace=True)
            
        if "Dst IP" in self.df.columns:
            self.df.drop(["Dst IP"], axis=1, inplace=True)
            
        if "Timestamp" in self.df.columns:
            self.df.drop(["Timestamp"], axis=1, inplace=True)
            
        self.drop_duplicate_columns()

        self.drop_bad_elements()
        
        print(self.df.columns)

        self.x = self.df.drop(["Label"], axis=1)
        self.y = self.df["Label"]
        
        # replace No Label with 0
        self.y = self.y.replace("No Label", 2)

        labels = set(self.y)

        print(f"labels: {labels}")
        
        print(self.x)
        
        #cast to float
        self.x["Src Port"] = self.x["Src Port"].astype(float)
        self.x["Dst Port"] = self.x["Dst Port"].astype(float)
        self.x["Protocol"] = self.x["Protocol"].astype(float)

        self.drop_bad_elements_x()

        print(self.x)
        if self.do_save:
            self.save_data()

    # Override
    def save_data(self):
        aux_df = self.df
        aux_df.drop(["Label"], axis=1, inplace=True)

        if self.y is not None:
            aux_y = pd.DataFrame(self.y, columns=["Label"])
            aux_y.to_csv(
                f"apolo/preprocesing/data/save/data_our/{self.name_save}_y.csv",
                index=False,
            )

        aux_df = pd.concat([aux_df, aux_y], axis=1)

        aux_df.to_csv(
            f"apolo/preprocesing/data/save/data_our/{self.name_save}.csv", index=False
        )
    
    def load_data(self):
        df = pd.read_csv(f"apolo/preprocesing/data/save/data_our/{self.name_load}.csv")
        y = pd.read_csv(f"apolo/preprocesing/data/save/data_our/{self.name_load}_y.csv")

        return df, y
