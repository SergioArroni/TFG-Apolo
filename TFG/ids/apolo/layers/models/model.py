# ========================== Model ==========================
#
#                   Author:  Sergio Arroni Del Riego
#
# ================================================================

# ==================> Imports
import time


# ==================> Classes
class Model:
    """Model

    This class is used to create a model object that will be used to train and test a model.

    Attributes:
        predictions: Predictions of the test data
        time_total: Total time of the training and testing of the model
        model_trained: Trained model
        dataset: Dataset name
        x_train: Training data
        y_train: Training labels
        x_test: Test data
        y_test: Test labels
        seed: Seed for the random state
    """

    def __init__(
        self,
        x_train: list,
        y_train: list,
        x_test: list,
        y_test: list,
        dataset: str,
        seed: int = 42,
    ) -> None:
        """__init__

        This method is used to initialize the Model class.

        Parameters:
            x_train: Training data
            y_train: Training labels
            x_test: Test data
            y_test: Test labels
            dataset: Dataset name
        Output:
            None
        """
        self.predictions = None
        self.time_total = None
        self.model_trained = None
        self.dataset = dataset
        self.x_train = x_train
        self.y_train = y_train
        self.x_test = x_test
        self.y_test = y_test
        self.seed = seed

    def exe(self) -> None:
        """exe

        This method is used to execute the model.

        Output:
            None
        """
        self.model_train_test()

    def model_train_test(self) -> None:
        """model_train_test

        TThis method is responsible for calling the model's training method and
        will also host any other functions that are performed on the model.

        Output:
            None
        """
        start = time.time()
        self.model_trained = self.expecific_model().fit(self.x_train, self.y_train)
        end_train = time.time()
        test_predictions = self.predict()
        end_predict = time.time()

        self.time_total = [
            end_train - start,
            end_predict - end_train,
            end_predict - start,
        ]
        self.predictions = test_predictions

    def predict(self, test_x: list = None) -> list:
        """predict

        This method is used to predict the labels of the test and training data.

        Parameters:
            test_x: Test data
        Output:
            y_test_predictions: Predicted labels of the test data
        """
        return (
            self.model_trained.predict(self.x_test)
            if test_x is None
            else self.model_trained.predict(test_x)
        )

    def expecific_model(self) -> object:
        """expecific_model

        This method right now just passes, but it will be defined by all children of this class and will hold each
        child's specific model.

        Output:
            object: The model object
        """
        pass
