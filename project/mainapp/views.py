import pandas
import joblib
import numpy

from django.shortcuts import HttpResponse, render
from django.templatetags.static import static


def interest(request):
    source = pandas.read_csv('project/mainapp/static/resources/questions.csv')
    questions = source['question'].tolist()

    batch = [questions[i:i + 6] for i in range(0, len(questions), 6)]

    return render(request, 'likert_scale.html', {'batch': batch})

def submit(request):
    if request.method == 'POST':
        batch = []

        for i in range(1, 5):
            strand_batch = []  # Create a batch for each strand
            for j in range(1, 7):
                answer = request.POST.get(f'likert{i}{j}')
                strand_batch.append(answer)
            batch.append(strand_batch)


        source = pandas.read_csv('project/mainapp/static/resources/questions.csv')
        strand = source['strand'].tolist()

        stem = 0    
        abm = 0
        humss = 0
        afa = 0
        he = 0
        ia = 0
        ict = 0

        for strand_batch, strand_name in zip(batch, strand):
            for value in strand_batch:
                match strand_name:
                    case 'humss':
                        humss += int(value)
                    case 'stem':
                        stem += int(value)
                    case 'abm':
                        abm += int(value)
                    case 'afa':
                        afa += int(value)
                    case 'ict':
                        ict += int(value)
                    case 'he':
                        he += int(value)
                    case 'ia':
                        ia += int(value)

        result = [stem, abm, humss, afa, he, ia, ict]
        model = joblib.load('project/mainapp/static/resources/demi.joblib')

        iresult = numpy.array(result).reshape(1, -1)
        fresult = model.predict(iresult)

        return render(request, "result.html", {"result": fresult})