from django.db import models
from django.contrib.auth.models import User


class Question(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    choicesCount = models.IntegerField()

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return f"{self.id} : {self.title}"


class Choice(models.Model):
    question = models.ForeignKey(Question, related_name="choices", on_delete=models.CASCADE)
    order = models.IntegerField()

    class Meta:
        unique_together = [
            ("question", "order")
        ]
        ordering = ("order",)

    def __str__(self):
        return f"{self.question} - {self.order}"


class VoteRecord(models.Model):
    choice = models.ForeignKey(Choice, related_name="voteRecords", on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_created=True)
