# ========================== Load Data & Models Utils ==========================
#
#                   Author:  Sergio Arroni Del Riego
#
# ==============================================================================

# ==================> Imports
import pandas as pd
import pickle


class UtilsLoad:
    """UtilsLoad

    This class is used to load the data and the models.

    Attributes:
        seed (int): seed for reproducibility

    """

    def __init__(self, seed: int = 42) -> None:
        """__init__

        This method is used to initialize the Utils class.

        Parameters:

        Output:
            None
        """
        self.seed = seed

    # ==================> Functions

    def load_data(self, path: list = None, seed: int = 42, json:dict = None) -> pd.DataFrame:
        """load_data

        This function loads the data from the path and returns a dataframe of the datasets

        Parameters:
            path (list): list of paths to the files
        Output:
            df (pd.DataFrame): dataframe with all the data
        """
        i = 0
        if json is not None:
            return self.load_data_cic(json)
        
        if path is not None:
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

    def load_data_cic(self, json: dict) -> pd.DataFrame:
        data = {
            "Flow Duration": [json.get("Flow Duration")],
            "Tot Fwd Pkts": [json.get("Tot Fwd Pkts")],
            "Tot Bwd Pkts": [json.get("Tot Bwd Pkts")],
            "TotLen Fwd Pkts": [json.get("TotLen Fwd Pkts")],
            "TotLen Bwd Pkts": [json.get("TotLen Bwd Pkts")],
            "Fwd Pkt Len Max": [json.get("Fwd Pkt Len Max")],
            "Fwd Pkt Len Min": [json.get("Fwd Pkt Len Min")],
            "Fwd Pkt Len Mean": [json.get("Fwd Pkt Len Mean")],
            "Fwd Pkt Len Std": [json.get("Fwd Pkt Len Std")],
            "Bwd Pkt Len Max": [json.get("Bwd Pkt Len Max")],
            "Bwd Pkt Len Min": [json.get("Bwd Pkt Len Min")],
            "Bwd Pkt Len Mean": [json.get("Bwd Pkt Len Mean")],
            "Bwd Pkt Len Std": [json.get("Bwd Pkt Len Std")],
            "Flow Byts/s": [json.get("Flow Byts/s")],
            "Flow Pkts/s": [json.get("Flow Pkts/s")],
            "Flow IAT Mean": [json.get("Flow IAT Mean")],
            "Flow IAT Std": [json.get("Flow IAT Std")],
            "Flow IAT Max": [json.get("Flow IAT Max")],
            "Flow IAT Min": [json.get("Flow IAT Min")],
            "Fwd IAT Tot": [json.get("Fwd IAT Tot")],
            "Fwd IAT Mean": [json.get("Fwd IAT Mean")],
            "Fwd IAT Std": [json.get("Fwd IAT Std")],
            "Fwd IAT Max": [json.get("Fwd IAT Max")],
            "Fwd IAT Min": [json.get("Fwd IAT Min")],
            "Bwd IAT Tot": [json.get("Bwd IAT Tot")],
            "Bwd IAT Mean": [json.get("Bwd IAT Mean")],
            "Bwd IAT Std": [json.get("Bwd IAT Std")],
            "Bwd IAT Max": [json.get("Bwd IAT Max")],
            "Bwd IAT Min": [json.get("Bwd IAT Min")],
            "Fwd PSH Flags": [json.get("Fwd PSH Flags")],
            "Bwd PSH Flags": [json.get("Bwd PSH Flags")],
            "Fwd URG Flags": [json.get("Fwd URG Flags")],
            "Bwd URG Flags": [json.get("Bwd URG Flags")],
            "Fwd Header Len": [json.get("Fwd Header Len")],
            "Bwd Header Len": [json.get("Bwd Header Len")],
            "Fwd Pkts/s": [json.get("Fwd Pkts/s")],
            "Bwd Pkts/s": [json.get("Bwd Pkts/s")],
            "Pkt Len Min": [json.get("Pkt Len Min")],
            "Pkt Len Max": [json.get("Pkt Len Max")],
            "Pkt Len Mean": [json.get("Pkt Len Mean")],
            "Pkt Len Std": [json.get("Pkt Len Std")],
            "Pkt Len Var": [json.get("Pkt Len Var")],
            "FIN Flag Cnt": [json.get("FIN Flag Cnt")],
            "SYN Flag Cnt": [json.get("SYN Flag Cnt")],
            "RST Flag Cnt": [json.get("RST Flag Cnt")],
            "PSH Flag Cnt": [json.get("PSH Flag Cnt")],
            "ACK Flag Cnt": [json.get("ACK Flag Cnt")],
            "URG Flag Cnt": [json.get("URG Flag Cnt")],
            "CWE Flag Count": [json.get("CWE Flag Count")],
            "ECE Flag Cnt": [json.get("ECE Flag Cnt")],
            "Down/Up Ratio": [json.get("Down/Up Ratio")],
            "Pkt Size Avg": [json.get("Pkt Size Avg")],
            "Fwd Seg Size Avg": [json.get("Fwd Seg Size Avg")],
            "Bwd Seg Size Avg": [json.get("Bwd Seg Size Avg")],
            "Fwd Byts/b Avg": [json.get("Fwd Byts/b Avg")],
            "Fwd Pkts/b Avg": [json.get("Fwd Pkts/b Avg")],
            "Fwd Blk Rate Avg": [json.get("Fwd Blk Rate Avg")],
            "Bwd Byts/b Avg": [json.get("Bwd Byts/b Avg")],
            "Bwd Pkts/b Avg": [json.get("Bwd Pkts/b Avg")],
            "Bwd Blk Rate Avg": [json.get("Bwd Blk Rate Avg")],
            "Subflow Fwd Pkts": [json.get("Subflow Fwd Pkts")],
            "Subflow Fwd Byts": [json.get("Subflow Fwd Byts")],
            "Subflow Bwd Pkts": [json.get("Subflow Bwd Pkts")],
            "Subflow Bwd Byts": [json.get("Subflow Bwd Byts")],
            "Init Fwd Win Byts": [json.get("Init Fwd Win Byts")],
            "Init Bwd Win Byts": [json.get("Init Bwd Win Byts")],
            "Fwd Act Data Pkts": [json.get("Fwd Act Data Pkts")],
            "Fwd Seg Size Min": [json.get("Fwd Seg Size Min")],
            "Active Mean": [json.get("Active Mean")],
            "Active Std": [json.get("Active Std")],
            "Active Max": [json.get("Active Max")],
            "Active Min": [json.get("Active Min")],
            "Idle Mean": [json.get("Idle Mean")],
            "Idle Std": [json.get("Idle Std")],
            "Idle Max": [json.get("Idle Max")],
            "Idle Min": [json.get("Idle Min")],
            "Label": [json.get("Label")]
        }
        
        df = pd.DataFrame(data)
        return df