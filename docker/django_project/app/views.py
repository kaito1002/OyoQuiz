from django.shortcuts import render


def index(request):
    context = {
        "sample_key": "sample_value"
    }
    return render(request, 'index.html', context)


def exercise(request, year: int, page_id: int):
    context = {
        "id": page_id,
        "year": year,
        "select_1": "hoge",
        "select_2": "foo",
        "select_3": "fuga",
        "select_4": "huge",
        "ex_number": 5,
        "paragraph": "ほげほげとはなにか?",
        "selections": [
            {"key": "ア", "value": "hoge"},
            {"key": "イ",  "value": "foo"},
            {"key": "ウ", "value": "fuga"},
            {"key": "エ",  "value": "huge"},
        ]
    }
    return render(request, 'exercise.html', context)


def answer(request, year: int, page_id: int):
    context = {
        "next": page_id + 1,
        "year": year,
        "answer": "ア",
        "description": "ほげとはhogeのことである.",
    }
    return render(request, 'answer.html', context)


def judge(request):
    context = {
        "percentage": 80,
        "comment": "大変良くできました."
    }
    return render(request, 'judge.html', context)

def top(request):
    context = {
        "morning": "午前",
        "afternoon": "午後"
    }

    return render(request, 'top.html', context)
