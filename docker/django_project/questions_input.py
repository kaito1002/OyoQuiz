from app.models import Exam
from app.models import Question
from config.settings import BASE_DIR
import csv
import os

datas = os.path.join(BASE_DIR, "datas")


def read_all():
    for path in os.listdir(datas):
        year, type = [int(x) for x in path[:-4].split("_")]
        read_exam(year, type)


def read_exam(year, type):
    with open(os.path.join(datas, f"{year}_{type}.csv"), "r") as f:
        questions = [_ for _ in csv.reader(f)]

    exam = Exam.objects.get_or_create(
        year=int(year),
        type=int(type),
        question_number=len(questions)
        )[0]

    print(exam)
    for i in range(len(questions)-1):
        Question.objects.get_or_create(
            statement=questions[i][0],
            description=questions[i][1],
            answer=int(questions[i][2]),
            select1=questions[i][3],
            select2=questions[i][4],
            select3=questions[i][5],
            select4=questions[i][6],
            question_id=i,
            exam=exam
        )
