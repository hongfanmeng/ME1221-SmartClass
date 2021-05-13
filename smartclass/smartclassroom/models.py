from django.db import models
from django.contrib.auth.models import User

# Create your models here.

FEEDBACK_CHOICE = [('faster', 'faster'), ('slower', 'slower'),
                   ('notClear', 'notClear'), ('notUnderstand', 'notUnderstand')]


class Feedback(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    feedbackType = models.CharField(choices=FEEDBACK_CHOICE, max_length=20)

    class Meta:
        ordering = ('created',)


class Question(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    choicesCount = models.IntegerField()

    class Meta:
        ordering = ('created',)


class Choice(models.Model):
    question = models.ForeignKey(Question, related_name="choices", on_delete=models.CASCADE)
    order = models.IntegerField()
    voteCount = models.IntegerField()

    class Meta:
        unique_together = [
            ("question", "order")
        ]
        ordering = ("order",)


class UserVote(models.Model):
    choice = models.ForeignKey(Choice, related_name="user_votes", on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
