import pandas

from django.shortcuts import HttpResponse, render
from django.templatetags.static import static


def interest(request):
    source = pandas.read_csv("project/mainapp/static/resources/questions.csv")
    questions = source['question'].tolist()

    batch = [questions[i:i + 6] for i in range(0, len(questions), 6)]

    return render(request, 'likert_scale.html', {'batch': batch})

def submit(request):
    return render(request, 'proceed.html')

def results(request):
    pass