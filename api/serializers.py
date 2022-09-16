from rest_framework import serializers
from base.models import Ability, Answers, MinimumAbilitiesReviewedPerDay, Topic


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
class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = ('id', 'topic')

class AbilitySerializer(serializers.ModelSerializer):
    answers_set = AnswersSerializer(many=True, read_only=True)
    #topico = TopicSerializer(many=True, read_only=True)
    class Meta:
        model = Ability
        depth = 1
        fields = ('id', 'ability', 'n_times_reviewed', 'created_at', 'answers_set', 'topic')
        
class NTimesReviewedSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Ability
        #depth = 1
        fields = '__all__'#('id', 'ability', 'n_times_reviewed', 'created_at')

class MinimumAbilitiesReviewedPerDaySerializer(serializers.ModelSerializer):
    class Meta:
        model = MinimumAbilitiesReviewedPerDay
        fields = '__all__'