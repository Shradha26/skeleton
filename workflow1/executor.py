from implementation.serial_executor import SerialExecutor
from workflow1.tasks.task1 import Task1
from workflow1.tasks.task2 import Task2


class WorkflowExecutor(SerialExecutor):
    def __init__(self):
        super().__init__()
        self.order = ["task1", "task2"]
        self.taskmap = {"task1": Task1, "task2": Task2}

    def run(self):
        for task in self.order:
            task_obj = self.taskmap[task](None)
            task_obj.execute()