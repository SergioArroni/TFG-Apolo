from layers import MAB
from utils import *


# Main function
def main() -> None:
    # Train the MAB
    df_preprocessed = UtilsLoad.load_dataset(
        dataset_name="CIC-IDS_2017_MAB", dataset_type="CIC_2017"
    )
    mab = MAB(n_arms=5, n_clusters=2)
    mab.train(df_preprocessed.x_train, df_preprocessed.y_train)


# Main function call
if __name__ == "__main__":
    main()
