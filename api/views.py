#Cómo solucionar
#-traer json con valores de Ability y de Answers
#--Tal vez uniendo dos queryset en uno...
#--Que la instancia del queryset sea una tabla compuesta
#  por las 2 tablas 
from base.models import Ability, AfterWhenToReview, Answers, ScheduleAbilities, Topic, Reviewed, MinimumAbilitiesReviewedPerDay, TypeOfAbility, Diary, Goal
from .serializers import AbilitySerializer, AnswersSerializer, DiarySerializer, GoalSerializer, NTimesReviewedSerializer, MinimumAbilitiesReviewedPerDaySerializer, TopicSerializer, TypeOfAbilitySerializer, GoalSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.db.models import Count, Sum
from django.utils import timezone
from rest_framework.renderers import JSONRenderer
import json
import csv
from .ways_to_present_abilities.ways_to_present_abilities import *#get_topics_at_random_with_memory
import datetime 

import json
from numpy import random

def choose_abilities1(n_total_abilities):
    n_abilities = random.randint(5, 25)
    # print('n_abilities to present')
    # print(n_abilities)
    random_idxs = random.choice(n_total_abilities, size=n_abilities)
    return random_idxs
    
@api_view(['GET'])
def getTopics(request):
    topics = Topic.objects.all()
    serialized_topics = TopicSerializer(topics, many=True)
    # print('serialized_topics')
    # print(serialized_topics)
    return Response(serialized_topics.data)

@api_view(['GET'])
def getData(request, id_topic=None):
    print('timezone.now().date() timedelta(days=3)')
    print(timezone.now().date() + datetime.timedelta(days=3))
    print('timezone.now().time()')
    
    #TODO:Aquí va el bandit para elegir entre distintas formas de presentar
    # habilidades
    #db_response = get_topics_at_random_with_memory()
    db_response = get_abilities_by_schedule2()
    serialized = AbilitySerializer(db_response, many=True)

    return Response(serialized.data)

@api_view(['GET'])
def getMetric(request, metric):
    # print('HOLAAAA')
    if metric == 'total-abilities':
        metric = len(Ability.objects.all())
    
    elif metric == 'abilities-by-day':
        metric = Ability.objects.values('created_at__date').annotate(dcount=Count('id')).order_by('created_at__date')
    
    elif metric == 'abilities-reviewed-by-day':
       metric = Reviewed.objects.values('updated_at__date').annotate(dcount=Count('id')).order_by('updated_at__date')#.values('ability', 'updated_at')#.order_by('created_at__date')
    #    print('metriiiiic')
    #    print(metric)
    print('metric')
    print(metric)
    return Response({'metric':metric})

@api_view(['GET'])
def getMinimumNumberOfAbilitiesReviewedToday(request):
    try:
        marpd = MinimumAbilitiesReviewedPerDay.objects.latest('datetime')
        serialized = MinimumAbilitiesReviewedPerDaySerializer(marpd, many=False)
        return Response(serialized.data)
    except:
        print('Seems there is not data in MinimumAbilitiesReviewedPerDay table')
        return Response({'status':'200'})
    # print('marpd')
    # print(serialized)
    



@api_view(['GET'])
def getAbilitiesByTopic(request):

    #random_indexes = choose_abilities1(100)
    
        
    #db_response = Ability.objects.filter(topic=id_topic, n_times_reviewed=0, id__in=random_indexes)#.filter(id=2)#.values('ability', 'n_times_reviewed', 'answers')
    
    #db_response = Ability.objects.all().values('topic').annotate(n_abilities_by_topic=Count('topic'))#all().values('ability', 'created_at','topic','updated_at').aggregate(dcount=Count('topic'))#filter(created_at__date=str(timezone.now().date()))#order_by('n_times_reviewed', '-created_at__date')
    db_response = Ability.objects.filter(created_at__date__lte=timezone.now().date()).values('topic').annotate(n_abilities_by_topic=Count('topic'))#all().values('ability', 'created_at','topic','updated_at').aggregate(dcount=Count('topic'))#filter(created_at__date=str(timezone.now().date()))#order_by('n_times_reviewed', '-created_at__date')
    #print(db_response)

    #serialized = AbilitySerializer(db_response, many=True)
    #print('type of serialized.data')
    #print(type(serialized))
    # print('QUEEE CARAJOS')
    # print('db_response abilities by topic')
    #print(db_response)
    # for row in db_response:
    #     print(row)#, row.dcount, row.topic)#, row.dcount, row.topic)
    return Response(db_response)



@api_view(['GET'])
def getAbilitiesReviewedToday(request):
    abilities_reviewed_today = Reviewed.objects.annotate(dcount=Count('id')).values().order_by('-id')
    # print(abilities_reviewed_today)
    return Response({'success':'true'})


@api_view(['GET'])
def getTypesOfAbilities(request):
    types_of_abilities = TypeOfAbility.objects.all()
    serialized = TypeOfAbilitySerializer(types_of_abilities, many=True)

    return Response(serialized.data)

@api_view(['GET'])
def getDiaryData(request):
    diary = Diary.objects.all().order_by('created_at')
    serialized = DiarySerializer(diary, many=True)
    return Response(serialized.data)



@api_view(['POST'])
def getPostData(request):
    
    serialized = AbilitySerializer(data=request.data)
    
    if serialized.is_valid():
        # print(request.data)#POST.get('saludo'))
        
        ability_reviewed = Reviewed(ability=Ability(id=request.data['id']), n_times_reviewed=request.data['n_times_reviewed'] + 1)#.objects.get(id=request.data['id'])
        ability_reviewed.save()
        ability = Ability.objects.get(id=request.data['id'])
        ability.n_times_reviewed = request.data['n_times_reviewed']

        ability.answer_correctness = request.data['answer_correctness']
        ability.answers_set.update(answer='\n'.join(request.data['answers_set'][0]['answer']))
        ability.ability =request.data['ability']
        print("request.data")
        print(request.data)
        print('ability.days_to_present_again')
        print(ability.days_to_present_again)
        ability.difficulty = request.data['difficulty']
        try:
            if request.data['answer_correctness'] > 7:
                fib_seq = string_to_list()
                idx_actual_fib_number = fib_seq.index(ability.days_to_present_again)
                if idx_actual_fib_number < len(fib_seq) - 1:
                    print('before')
                    print('ability.days_to_present_again')
                    print(ability.days_to_present_again)
                    ability.days_to_present_again = fib_seq[idx_actual_fib_number + 1]
                    print('after')
                    print('ability.days_to_present_again')
                    print(ability.days_to_present_again)
            elif request.data['answer_correctness'] < 4:
                print('Tuvo una calificación <= 4 de la respuesta')
                fib_seq = string_to_list()
                idx_actual_fib_number = fib_seq.index(ability.days_to_present_again)
                if idx_actual_fib_number > 0:
                    print('before')
                    print('ability.days_to_present_again')
                    print(ability.days_to_present_again)
                    ability.days_to_present_again = fib_seq[idx_actual_fib_number - 1]
                    print('after')
                    print('ability.days_to_present_again')
                    print(ability.days_to_present_again)
        except:
            print('seems like is comming from edit section :)')

        ability.save()
        

        today_count_reviewed_abilities = Reviewed.objects.values('updated_at__date').annotate(dcount=Count('id')).order_by('-updated_at__date')#.values('ability', 'updated_at')#.order_by('created_at__date')
        # print('today_count_reviewed_abilities[-1]')
        # print(today_count_reviewed_abilities[0]['dcount'])
        # print(ability_reviewed)
        #ability_reviewed.n_times_reviewed += 1
        #ability_reviewed.save()
        
        # print('ability.n_times_reviewed')
        # print(ability_reviewed.n_times_reviewed)
        #ability = Ability.objects.filter(id=request.data['id'])
        #serialized = NTimesReviewedSerializer(data=ability, many=True)
        #print('serialized 2')
        #print(serialized)
        #if serialized.is_valid():
         #   print("ENTROOO")
        return Response({'ability': ability_reviewed.ability.ability, 'n_times_reviewed':ability_reviewed.n_times_reviewed,'n_reviewed_abilities_today':today_count_reviewed_abilities[0]['dcount']})
    return Response({'error':'invalid request 400'})


@api_view(['POST'])
def getPostAbility(request):
    serialized = AbilitySerializer(data=request.data)

    if serialized.is_valid():
        print('yeah! inside')
        
        ab = Ability(ability=request.data['ability'])
        ab.save()
        print('hasta aca?')
        if request.data['answer'] != '':
            an = ab.answers_set.create(answer=request.data['answer'])
        ab.topic = Topic(id=request.data['selection'])
        ab.difficulty = request.data['difficulty']
        ab.type = TypeOfAbility(id=request.data['type'])
        ab.save()

        #sa = ScheduleAbilities(ability=Ability(id=ab.id), presented_at=None)
        #sa.save()
    return Response({'success':'true'})

@api_view(['GET'])
def getGoals(request):
    g = Goal.objects.get(id=15)
    print('type(g)')
    print(type(g))
    #serialized_goals = GoalSerializer(g)#, many=True) 
    #content = JSONRenderer().render(serialized_goals.data)
    print('content')
    g = json.loads(g.goal.replace("'", '"'))
    print(g)
    print(type(g))
    # g = dict(g)
    # print(type(g))
    return Response(g)

@api_view(['POST'])
def postGoals(request):
    print('nada?')
    print(request.data)
    g = Goal(goal=request.data)
    g.save()
    return Response({"status":200})


@api_view(['POST'])
def postInDiary(request):
    last_day = Diary.objects.last()
    if last_day.created_at.date() == timezone.now().date():
        last_day.description += request.data['description']
        last_day.save()
    #print(request.data)
    
    #print(type(last_day))
    else:
        diary = Diary(description=request.data['description'])
        #last_day.description += request.data['description']
        diary.save()
    return Response({'status':'200 OK'})