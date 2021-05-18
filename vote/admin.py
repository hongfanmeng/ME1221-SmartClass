from django.contrib import admin
from .models import Question, Choice, VoteRecord


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'choicesCount', 'created']
    list_display_links = ['title']
    ordering = ['id']


@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ['question', 'order', 'voteCount']
    ordering = ['question', 'order']

    def voteCount(self, choice):
        return choice.voteRecords.count()


@admin.register(VoteRecord)
class VoteUserAdmin(admin.ModelAdmin):
    def order(self, voteRecord):
        return voteRecord.choice.order

    def question(self, voteRecord):
        return voteRecord.choice.question

    list_display = ['question', 'order', 'user', 'created']
    ordering = ['-created']
