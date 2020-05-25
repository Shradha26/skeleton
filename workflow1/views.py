from django.shortcuts import render
from workflow1.executor import WorkflowExecutor
from django.http import HttpResponse


def index(request):
    #print(request.GET["id"])
    executor = WorkflowExecutor()
    executor.run()
    return HttpResponse("Finished executing workflow")