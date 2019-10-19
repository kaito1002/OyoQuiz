from django.db import models


class Exam(models.Model):
    year = models.IntegerField()             # 年度
    type = models.IntegerField()             # 0: 午前, 1: 午後
    question_number = models.IntegerField()  # 問題数

    def __repr__(self):
        return "{}: {}, {}".format(self.pk, self.year, self.question_number)

    __str__ = __repr__


class Question(models.Model):
    statement = models.TextField()                # 問題文
    description = models.TextField(null=True)     # 解説
    answer = models.IntegerField()                # 正答 1 to 4
    select1 = models.CharField(max_length=128)         # 選択肢1
    select2 = models.CharField(max_length=128)         # 選択肢2
    select3 = models.CharField(max_length=128)         # 選択肢3
    select4 = models.CharField(max_length=128)         # 選択肢4
    question_id = models.IntegerField()  # 問題番号
    exam = models.ForeignKey(
        Exam,
        on_delete=models.CASCADE,
        related_name="questions",
    )

    @property
    def answer_str(self) -> str:
        if self.answer == 1:
            return "ア"
        elif self.answer == 2:
            return "イ"
        elif self.answer == 3:
            return "ウ"
        else:  # 1 - 4 以外は考慮しない
            return "エ"

    def __repr__(self):
        return "{}: {} => {}".format(self.exam, self.question_id, self.answer_str)

    __str__ = __repr__
