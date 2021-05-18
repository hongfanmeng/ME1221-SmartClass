from django.db import models

FEEDBACK_CHOICE = [('faster', 'faster'), ('slower', 'slower'),
                   ('notClear', 'notClear'), ('notUnderstand', 'notUnderstand')]


class Feedback(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    feedbackType = models.CharField(choices=FEEDBACK_CHOICE, max_length=20)

    class Meta:
        ordering = ('created',)
