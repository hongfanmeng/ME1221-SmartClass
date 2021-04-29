from rest_framework import serializers
from smartclass.smartclassroom.models import Feedback, Question, Choice, FEEDBACK_CHOICE


class ChoiceGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ['order', 'voteCount']


class VoteSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)

    id = serializers.IntegerField(read_only=True)
    created = serializers.DateTimeField(read_only=True)
    choices = ChoiceGetSerializer(many=True, read_only=True)

    choiceCount = serializers.IntegerField(write_only=True, max_value=6)

    class Meta:
        model = Question
        fields = ['id', 'title', 'created', 'choices']

    def create(self, validated_data):
        choiceCount = validated_data.pop("choiceCount")
        question = Question.objects.create(**validated_data)
        for i in range(choiceCount):
            Choice.objects.create(question=question, order=i, voteCount=0)
        return question

    def update(self, instance, validated_data):
        return super(instance, validated_data)


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        field = ['feedbackType, created']
