import pandas

from django.shortcuts import HttpResponse, render
from django.templatetags.static import static


def interest(request):
    batch = [
        ['question1a', 'question2a', 'question3a', 'question4a', 'question5a', 'question6a'],
        ['question1b', 'question2b', 'question3b', 'question4b', 'question5b', 'question6b'],
        ['question1c', 'question2c', 'question3c', 'question4c', 'question5c', 'question6c'],
        ['question1d', 'question2d', 'question3d', 'question4d', 'question5d', 'question6d'],
    ]

    return render(request, 'likert_scale.html', {'batch': batch})

def submit_interest(request):
    return render(request, 'proceed.html')

def aptitude(request):
    batch = []

    for i in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']:
        questions = []
        for j in range(10):
            questions.append(f"question{j}{i}")

        batch.append(questions)

    return render(request, 'aptitude.html', {'batch': batch})

def submit_aptitude(request):
    return render(request, 'result.html')