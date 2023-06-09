from apolo.layers import MAB
from utils import DataSelector
from apolo.layers.models import (
    RandomForest,
    DecisionTree,
    NaiveBayes,
    LogisticRegressionModel,
    MLP,
)
from apolo.model_train import ApoloTrainer
from apolo.model_predict import ApoloPredict


# Main function
def main() -> None:
    # Train the MAB
    seed = 42
    data_prep = DataSelector(seed=seed)
    apolo = ApoloTrainer(seed=seed)
    testing = ApoloPredict()
    list_load_request = [
        "apolo/preprocesing/data/CIC_2017/Thursday-WorkingHours-Afternoon-Infilteration.pcap_ISCX.csv"
    ]
    testing.classify_request(list_load_request=list_load_request)

    """    
    df_preprocessed = data_prep.load_dataset(
        name="CIC-IDS_2017_MAB", dataset_type="Data_Our"
    )

        apolo.train_model(
        X_test=df_preprocessed.x_test,
        y_test=df_preprocessed.y_test,
        X_train=df_preprocessed.x_train,
        y_train=df_preprocessed.y_train,
    ) 
    apolo.test_model(df_preprocessed=df_preprocessed)
    """


# Main function call
if __name__ == "__main__":
    main()
