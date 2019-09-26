from django.shortcuts import render


def index(request):
    context = {
        "sample_key": "sample_value"
    }
    return render(request, 'index.html', context)
