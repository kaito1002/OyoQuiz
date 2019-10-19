from django.shortcuts import render
from .models import Exam, Question


def index(request):
    context = {
        "sample_key": "sample_value"
    }
    return render(request, 'index.html', context)


def exercise(request, year: int, e_type: int, page_id: int):
    exam = Exam.objects.get(year=year, type=e_type)
    question = Question.objects.get(exam=exam, question_id=page_id)

    context = {
        "id": page_id,
        "year": year,
        "type": e_type,
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


def answer(request, year: int, e_type: int, page_id: int):
    exam = Exam.objects.get(year=year, type=e_type)
    question = Question.objects.get(exam=exam, question_id=page_id)

    # session result data
    result = {}
    if "result" in request.session.keys():
        result = request.session["result"]

    if str(year) not in result.keys():
        result[str(year)] = {}

    if str(e_type) not in result[str(year)].keys():
        result[str(year)][str(e_type)] = {}

    user_answer = request.GET["answer"]  # ア ... エ
    is_correct = user_answer == question.answer_str
    is_end = not page_id >= exam.question_number
    result[str(year)][str(e_type)][str(page_id)] = is_correct
    request.session["result"] = result

    context = {
        "next": page_id + 1,
        "year": year,
        "type": e_type,
        "answer": question.answer_str,
        "is_correct": is_correct,
        "is_end": is_end,
        "description": question.description,
    }
    return render(request, 'answer.html', context)


def judge(request, year: int, e_type: int):
    results = list(request.session["result"][str(year)][str(e_type)].values())
    request.session["result"] = {}  # リセット

    num = len(results)
    corrects_num = filter(lambda x: x, results)
    corrects_num = len(list(corrects_num))

    context = {
        "percentage": 100 * (corrects_num / num),
        "comment": "大変良くできました."
    }
    return render(request, 'judge.html', context)


def top(request):
    exams = [{
        "year": x.year,
        "type": x.type,
        "type_str": "午前" if x.type == 0 else "午後"
    } for x in Exam.objects.all()]
    context = {
        "exams": exams,
    }

    return render(request, 'top.html', context)
