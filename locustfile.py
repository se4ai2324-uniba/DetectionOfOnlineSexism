from locust import HttpUser, task, between
import random

class DetectionOfOnlineSexismUser(HttpUser):
    """
    This class represents a user for simulating web traffic, specifically for testing
    various endpoints related to the detection of online sexism.
    """
    wait_time = between(1, 5)  # Setting wait time between tasks from 1 to 5 seconds.

    @task(1)
    def test_main_endpoint(self):
        """Task to test the main endpoint."""
        response = self.client.get("/")
        if response.status_code != 200:
            raise Exception("Failed to get the main endpoint description")
        response_json = response.json()
        expected_keys = ['title', 'description', 'version', 'available_endpoints']
        if not all(key in response_json for key in expected_keys):
            raise Exception("The main endpoint description response is missing some expected keys")

    @task(1)
    def main_endpoint_description(self):
        """Task to get a description of the main endpoint."""
        response = self.client.get("/task")
        if response.status_code != 200:
            raise Exception("Failed to get the main task description")
        response_json = response.json()
        expected_keys = ['title', 'description', 'pipeline', 'more_information']
        if not all(key in response_json for key in expected_keys):
            raise Exception("The main task description response is missing some expected keys")

    @task(1)
    def task_A_description(self):
        """Task to get a description of task A."""
        response = self.client.get("/task/A")
        if response.status_code != 200:
            raise Exception("Failed to get the task A description")
        response_json = response.json()
        expected_keys = ['title', 'description', 'model', 'metrics']
        if not all(key in response_json for key in expected_keys):
            raise Exception("The task A description response is missing some expected keys")
        
    @task(1)
    def task_B_description(self):
        """Task to get a description of task B."""
        response = self.client.get("/task/B")
        if response.status_code != 200:
            raise Exception("Failed to get the task B description")
        response_json = response.json()
        expected_keys = ['title', 'description', 'model', 'metrics']
        if not all(key in response_json for key in expected_keys):
            raise Exception("The task B description response is missing some expected keys")

    @task(1)
    def get_metrics_task_A(self):
        """Task to get metrics for task A."""
        response = self.client.get("/task/A/metrics")
        if response.status_code != 200:
            raise Exception("Metrics computation failed for task A")
        metrics = response.json()
        expected_keys = ["title", "model", "f1", "recall", "precision"]
        if not all(key in metrics for key in expected_keys):
            raise Exception("Metrics response for task A is incomplete")

    @task(1)
    def get_metrics_task_B(self):
        """Task to get metrics for task B."""
        response = self.client.get("/task/B/metrics")
        if response.status_code != 200:
            raise Exception("Metrics computation failed for task B")
        metrics = response.json()
        expected_keys = ["title", "model", "f1", "recall", "precision"]
        if not all(key in metrics for key in expected_keys):
            raise Exception("Metrics response for task B is incomplete")

    @task(1)
    def task_A_preprocessing(self):
        """Task to get preprocessing information for task A."""
        response = self.client.get("/task/A/preprocessing")
        if response.status_code != 200:
            raise Exception("Failed to get the task A preprocessing description")
        response_json = response.json()
        expected_keys = ["title", "tokenizer", "vectorizer", "lemmatizer"]
        if not all(key in response_json for key in expected_keys):
            raise Exception("The preprocessing description response for task A is incomplete")

    @task(1)
    def task_B_preprocessing(self):
        """Task to get preprocessing information for task B."""
        response = self.client.get("/task/B/preprocessing")
        if response.status_code != 200:
            raise Exception("Failed to get the task B preprocessing description")
        response_json = response.json()
        expected_keys = ["title", "tokenizer", "vectorizer", "lemmatizer"]
        if not all(key in response_json for key in expected_keys):
            raise Exception("The preprocessing description response for task B is incomplete")

    @task(3)
    def prediction_sexism(self):
        """Task to simulate prediction of sexism in a message."""
        message_sexism = [
            {"message": "When a girl gives you shit test, scare the shit out of her."},
            {"message": "The only thing lewd is your innuendo young lady."},
            {"message": "As a Jew. I can confirm I rape girls every night in the alleys Just kidding. You're a fucking moron rofl"},
            {"message": "Because she's a skank."},
            {"message": "Men are better at everything than women. Even when it comes to looks."}
        ]
        response = self.client.post("/prediction_sexism", json=message_sexism[random.randint(0, 4)])
        if response.status_code != 200:
            input_message = message_sexism["message"]
            raise Exception(f"Prediction failed for sentence: {input_message}")
        if "prediction" not in response.json():
            raise Exception(f"No mask in the prediction response for sentence: {input_message}")

    @task(3)
    def prediction_category(self):
        """Task to simulate prediction of sexism category in a message."""
        message_category = [
            {"message": "Fuck Claire McCaskill, she is a super twat. I am voting against her, and everyone else in Missouri should too."},
            {"message": "O come on there's no way any men are attracted to her shes a pig"},
            {"message": "I got <metoo-ed> holy shit lol. It's funny and also scarily possible."},
            {"message": "Asian women with power and self respect. Only happens on opposite day."},
            {"message": "I wish they'd thrown the commie race traitor bitch down & fucked her to death."}
        ]
        response = self.client.post("/prediction_category", json=message_category[random.randint(0, 4)])
        if response.status_code != 200:
            input_message = message_category["message"]
            raise Exception(f"Prediction failed for sentence: {input_message}")
        if "prediction" not in response.json():
            raise Exception(f"No mask in the prediction response for sentence: {input_message}")
