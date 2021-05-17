from rest_framework import serializers
from smartclass.smartclassroom.models import Feedback, Question, Choice, UserVote


class ChoiceGetSerializer(serializers.ModelSerializer):
    voteCount = serializers.SerializerMethodField(read_only=True)

    def get_voteCount(self, choice):
        return choice.userVotes.count()

    class Meta:
        model = Choice
        fields = ['order', 'voteCount']


class VoteSerializer(serializers.ModelSerializer):
    choicesCount = serializers.IntegerField(min_value=1, max_value=6)

    class Meta:
        model = Question
        fields = ['id', 'title', 'choicesCount']

    def create(self, validated_data):
        choiceCount = validated_data.get("choicesCount")
        question = Question.objects.create(**validated_data)
        for i in range(choiceCount):
            Choice.objects.create(question=question, order=i + 1)
        return question


class VoteDetailSerializer(serializers.ModelSerializer):
    order = serializers.IntegerField(write_only=True)
    choices = ChoiceGetSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = ['id', 'title', 'choicesCount', 'choices', 'order', ]
        read_only_fields = ['id', 'title', 'choicesCount', 'choices', 'created']

    def validate(self, attrs):
        instance = self.instance
        order = attrs.get('order')
        if 1 <= order <= instance.choicesCount:
            return attrs
        raise serializers.ValidationError(
            "order must between 1 and %d (the count of choices)" % instance.choicesCount)

    def update(self, instance, validated_data):
        order = validated_data.get('order')
        choices = instance.choices
        user = self.context.get('request').user
        for choice in choices.filter(order=order):
            UserVote.objects.filter(user=user).delete()
            UserVote.objects.create(choice=choice, user=user)
        return instance


class VoteStatusSerializer(serializers.ModelSerializer):
    hasVote = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Question
        fields = ['hasVote']

    def get_hasVote(self, question):
        user = self.context.get('request').user
        for choice in question.choices.all():
            if choice.userVotes.all().filter(user=user).exists():
                return True
        return False


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ['feedbackType', 'created']
