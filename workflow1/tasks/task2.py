from implementation.api_task import APITask


class Task2(APITask):
    def __init__(self, logger):
        super().__init__(logger)
        self.taskname = "Task2"

    def gather_input(self):
        print("Gathering input for Task2")
        self.endpoint = "https://superheroapi.com/api/2933400190062020/15"
        self.timeout = 23
        print("Endpoint: " + self.endpoint)
        print("Timeout: " + str(self.timeout))

    def execute(self):
        self.gather_input()
        print("Starting task2")
        return super().execute("get", 200)
