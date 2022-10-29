from rest_framework import serializers
from base.models import Ability, Answers, Diary, MinimumAbilitiesReviewedPerDay, Topic, TypeOfAbility, Goal, TimeStudyingTopic


# class AbilitySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Ability
#         fields = '__all__'#('ability', 'n_times_reviewed', 'ability')
#         depth = 1

class AnswersSerializer(serializers.ModelSerializer):
    #ability = serializers.PrimaryKeyRelatedField(queryset=Ability.objects.all()) 
    class Meta:
        model = Answers
        fields = '__all__'
        fields = ('id', 'answer', 'created_at')
        #depth = 1

class TimeStudyingTopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeStudyingTopic
        fields = ('topics', 'time_in_minutes', 'description')
        
class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = ('id', 'topic')


class TypeOfAbilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeOfAbility
        fields = ('id', 'type')

        
class AbilitySerializer(serializers.ModelSerializer):
    answers_set = AnswersSerializer(many=True, read_only=True)
    #topico = TopicSerializer(many=True, read_only=True)
    class Meta:
        model = Ability
        depth = 1
        fields = ('id', 'ability', 'n_times_reviewed', 'created_at', 'difficulty', 'answer_correctness', 'last_presentation_at', 'days_to_present_again', 'type', 'answers_set', 'topic')
        
class NTimesReviewedSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Ability
        #depth = 1
        fields = '__all__'#('id', 'ability', 'n_times_reviewed', 'created_at')

class MinimumAbilitiesReviewedPerDaySerializer(serializers.ModelSerializer):
    class Meta:
        model = MinimumAbilitiesReviewedPerDay
        fields = '__all__'

class DiarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Diary
        fields = '__all__'

class GoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goal 
        fields = ('goal',)