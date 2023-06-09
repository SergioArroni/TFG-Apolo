# ========================== MAB ==========================
#
#                   Author:  Sergio Arroni Del Riego
#
# ================================================================

# ==================> Imports
import numpy as np

# from datasets import preprocess_dataset, datasets_types
# from scipy.stats import beta as beta_dist

from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.metrics import f1_score, recall_score, roc_auc_score

from apolo.layers.clustering import KMeansCluster
from utils import UtilsLoad


# ==================> Classes
class MAB:
    """MAB

    This class is used to implement the Multi-Armed Bandit algorithm.

    Attributes:
        n_arms (int): number of arms
        n_clusters (int): number of clusters
        arms (list): list of arms
        cluster_centers (list): list of cluster centers
        cluster_assignments (list): list of cluster assignments
        reward_sums (dict): dictionary of reward sums
        alpha (list): list of alpha values
        beta (list): list of beta values
        kmeans (object): KMeans object
    """

    def __init__(self, arms: list, n_clusters: int = 2, seed: int = 42) -> None:
        """__init__

        This method is used to initialize the MAB class.

        Parameters:
            n_arms (int): number of arms
            n_clusters (int): number of clusters
            seed (int): seed for reproducibility
        Output:
            None
        """
        self.n_clusters = n_clusters
        self.arms = arms
        self.n_arms: int = len(self.arms)
        self.cluster_centers = None
        self.cluster_assignments = None
        self.reward_sums = {}
        self.alpha = np.ones(self.n_arms)
        self.beta = np.ones(self.n_arms)
        self.kmeans: KMeansCluster = KMeansCluster(
            k=self.n_clusters, seed=seed
        ).expecific_model()
        self.usl: UtilsLoad = UtilsLoad()

        for cluster in range(self.n_clusters):
            self.reward_sums[cluster] = np.zeros(self.n_arms)

    def train(self, X_train: list, y_train: list, X_test: list, y_test: list) -> None:
        """train

        This method is used to train the MAB.

        Parameters:
            X_train: Training data.
            y_train: Training labels.
            X_test: Testing data.
            y_test: Testing labels.
        Output:
            None
        """

        self.cluster_assignments = self.kmeans.fit_predict(X_train)
        self.cluster_centers = self.kmeans.cluster_centers_

        # Print the number of samples in each cluster
        for i in range(self.n_clusters):
            print(f"[Train] Cluster {i}: {np.sum(self.cluster_assignments == i)}")
            cluster_mask = self.cluster_assignments == i
            cluster_X_train = X_train[cluster_mask]
            cluster_y_train = y_train[cluster_mask]

            for arm in range(self.n_arms):
                print(f"Training arm {arm} on cluster {i}")
                arm_mask = cluster_y_train == arm
                arm_X_train = cluster_X_train[arm_mask]
                arm_y_train = cluster_y_train[arm_mask]
                if len(arm_X_train) > 0 and len(np.unique(arm_y_train)) > 1:
                    self.arms[arm].fit(arm_X_train, arm_y_train)
                else:
                    self.arms[arm].fit(X_train, y_train)

        # Set the arms rewards for each cluster
        for i in range(self.n_clusters):
            print(f"[Test] Cluster {i}: {np.sum(self.cluster_assignments == i)}")
            cluster_mask = self.cluster_assignments == i
            cluster_X_test = X_train[cluster_mask]
            cluster_y_test = y_train[cluster_mask]

            for arm in range(self.n_arms):
                print(f"Setting reward_sums arm {arm} on cluster {i}")
                arm_mask = cluster_y_test == arm
                arm_X_test = cluster_X_test[arm_mask]
                arm_y_test = cluster_y_test[arm_mask]
                if len(arm_X_test) > 0:
                    arm_y_pred = self.arms[arm].predict(arm_X_test)
                    self.reward_sums[i][arm] = np.mean(arm_y_pred == arm_y_test)
                else:
                    arm_y_pred = self.arms[arm].predict(X_test)
                    self.reward_sums[i][arm] = np.mean(arm_y_pred == y_test)

    def select_arm(self, cluster: int) -> int:
        """select_arm

        This method is used to select an arm.

        Parameters:
            cluster: Cluster to select the arm from.
        Output:
            Selected arm.
        """

        # Select the arm with the highest reward
        theta = np.zeros(self.n_arms)
        for arm in range(self.n_arms):
            theta[arm] = np.random.beta(
                self.alpha[arm] + self.reward_sums[cluster][arm],
                self.beta[arm] + 1 - self.reward_sums[cluster][arm],
            )

        return np.argmax(theta)

    def predict(self, X_test: list) -> tuple:
        """predict

        This method is used to predict the labels of the testing data.

        Parameters:
            X_test: Testing data.
        Output:
            y_pred: Predicted labels.
            arms: Selected arms.
        """

        # Select the arm for each sample
        arms = np.zeros(len(X_test))
        for i in range(len(X_test)):
            cluster = np.argmin(
                np.linalg.norm(self.cluster_centers - X_test[i], axis=1)
            )
            arms[i] = self.select_arm(cluster)

        # Predict using the selected arm
        y_pred = np.zeros(len(X_test))
        for arm in range(self.n_arms):
            arm_mask = arms == arm
            arm_X_test = X_test[arm_mask]
            if len(arm_X_test) > 0:
                y_pred[arm_mask] = self.arms[arm].predict(arm_X_test)

        return y_pred, arms

    def test(
        self,
        df_preprocessed: object,
        name: str = "apolo/results/MAB_test.txt",
        load_model: str = None,
    ) -> None:
        """test

        This method is used to test the MAB.

        Parameters:
            df_preprocessed: Preprocessed dataset.
            name: Name of the file where the results will be saved.
        Output:
            None
        """

        # Test the MAB
        if load_model is not None:
            model = self.usl.load_model(name=load_model)
            self.y_pred, self.selected_arms = model.predict(df_preprocessed.x_test)
        else:
            self.y_pred, self.selected_arms = self.predict(df_preprocessed.x_test)

        # Transform the y_pred values to 0 and 1 strings
        self.y_test = np.array([int(y) for y in df_preprocessed.y_test])
        self.y_pred = np.array([int(y) for y in self.y_pred])

        v = open(name, "a")

        v.write(
            "==============================================================================\n"
        )

        # Print y_pred unique values
        v.write(f"{np.unique(self.y_pred)}\n")

        # Print y_test unique values
        v.write(f"{np.unique(self.y_test)}\n")

        v.write(f"{classification_report(self.y_test, self.y_pred)}\n")

        v.write(f"Accuracy: {accuracy_score(self.y_test, self.y_pred)}\n")

        score = recall_score(self.y_test, self.y_pred, average="macro")
        v.write(f"Recall: {score}\n")

        score = f1_score(self.y_test, self.y_pred, average="macro")
        v.write(f"F1 Score: {score}\n")

        v.write(f"ROC AUC Score: {roc_auc_score(self.y_test, self.y_pred)}\n")

        v.close()

    def print_arms_test(self, name: str = "apolo/results/ARMS.txt") -> None:
        """print_arms_test

        This method is used to print the results of the arms.

        Parameters:
            name: Name of the file where the results will be saved.
        Output:
            None
        """

        v = open(name, "a")
        for i in range(self.y_pred.shape[0]):
            v.write(
                f"Selected arm: {self.selected_arms[i]}\tPredicted:{self.y_pred[i]}\tActual:{self.y_test[i]}"
            )
        v.close()
