from implementation.api_task import APITask


class Task1(APITask):
    def __init__(self, logger):
        super().__init__(logger)
        self.taskname = "Task1"

    def gather_input(self):
        print("Gathering input for task1")
        self.endpoint = "https://superheroapi.com/api/2933400190062020/5"
        self.timeout = 30
        print("Endpoint: " + self.endpoint)
        print("Timeout: " + str(self.timeout))

    def execute(self):
        self.gather_input()
        print("Starting task1")
        return super().execute("get", 200)
