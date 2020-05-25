from abstract.basic_task import BasicTask
from abc import abstractmethod
import requests
import json


class APITask(BasicTask):
    def __init__(self, logger):
        super(APITask, self).__init__(logger)
        self.endpoint, self.payload, self.timeout = None, None, None
        self.methods = {
            "post": lambda: requests.post(url=self.endpoint, payload=self.payload, timeout=self.timeout),
            "get": lambda: requests.get(url=self.endpoint, timeout=self.timeout),
            "delete": lambda: requests.get(url=self.endpoint, timeout=self.timeout)
        }

    @abstractmethod
    def gather_input(self):
        pass

    @abstractmethod
    def execute(self, type, code):
        try:
            response = self.methods[type]()
            if response.status_code != code:
                print("ERROR:" + response["response"])
                return False
            response = json.loads(response.content)
            print(response.get("powerstats"))
            return True
        except requests.exceptions.ConnectionError as e:
            print("ERROR:" + e.__repr__())
            return False
        except requests.exceptions.Timeout as e:
            print("ERROR:" + e.__repr__())
            return False
