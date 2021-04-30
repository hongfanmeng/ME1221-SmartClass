from rest_framework import serializers
from smartclass.smartclassroom.models import Feedback, Question, Choice, FEEDBACK_CHOICE


class ChoiceGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ['order', 'voteCount']


class ChoiceUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ['id']
        read_only_fields = ['voteCount']

    def update(self, instance, validated_data):
        instance.voteCount += 1
        instance.save()
        return instance


class VoteSerializer(serializers.ModelSerializer):
    choices = ChoiceGetSerializer(many=True, read_only=True)
    choiceCount = serializers.IntegerField(write_only=True, max_value=6, min_value=1)

    class Meta:
        model = Question
        fields = ['title', 'id', 'created', 'choices', 'choiceCount']

    def create(self, validated_data):
        choiceCount = validated_data.pop("choiceCount")
        question = Question.objects.create(**validated_data)
        for i in range(choiceCount):
            Choice.objects.create(question=question, order=i, voteCount=0)
        return question


class VoteDetailSerializer(serializers.ModelSerializer):
    order = serializers.IntegerField(write_only=True)
    choices = ChoiceGetSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = ['id', 'title', 'created', 'choices', 'order']
        read_only_fields = ['id', 'title', 'created']

    def validate(self, attrs):
        instance = self.instance
        order = attrs.get('order')

        if 0 <= order < instance.choices.count():
            return attrs
        raise serializers.ValidationError(
            "order must from 0 to %d" % (instance.choices.count() - 1))

    def update(self, instance, validated_data):
        order = validated_data.get('order')
        choices = instance.choices
        for choice in choices.filter(order=order):
            choice.voteCount += 1
            choice.save()
        return instance


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        field = ['feedbackType, created']
