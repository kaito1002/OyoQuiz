from django.shortcuts import render
from .models import Exam, Question


def index(request):
    context = {
        "sample_key": "sample_value"
    }
    return render(request, 'index.html', context)


def exercise(request, year: int, type: str, page_id: int):
    exam = Exam.objects.get(year=year, type=type)
    question = Question.objects.get(exam=exam, question_id=page_id)

    context = {
        "id": page_id,
        "year": year,
        "type": type,
        "ex_number": page_id,
        "paragraph": question.statement,
        "selections": [
            {"key": "ア", "value": question.select1},
            {"key": "イ", "value": question.select2},
            {"key": "ウ", "value": question.select3},
            {"key": "エ", "value": question.select4},
        ]
    }
    return render(request, 'exercise.html', context)


def answer(request, year: int, type: str, page_id: int):
    exam = Exam.objects.get(year=year, type=type)
    question = Question.objects.get(exam=exam, question_id=page_id)

    context = {
        "next": page_id + 1,
        "year": year,
        "type": type,
        "answer": question.answer_str,
        "description": question.description,
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
