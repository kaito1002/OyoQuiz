from django.shortcuts import render


def index(request):
    context = {
        "sample_key": "sample_value"
    }
    return render(request, 'index.html', context)

def exercise(request):
    context = {
        "select_1": 1,
        "select_2": 2,
        "select_3": 3,
        "select_4": 4,
        "ex_number": 5
    }
    return render(request, 'exercise.html', context)
