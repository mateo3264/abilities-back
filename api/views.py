#Cómo solucionar
#-traer json con valores de Ability y de Answers
#--Tal vez uniendo dos queryset en uno...
#--Que la instancia del queryset sea una tabla compuesta
#  por las 2 tablas 
from base.models import Ability, AfterWhenToReview, Answers, Topic, Reviewed, MinimumAbilitiesReviewedPerDay, TypeOfAbility, Diary
from .serializers import AbilitySerializer, AnswersSerializer, DiarySerializer, NTimesReviewedSerializer, MinimumAbilitiesReviewedPerDaySerializer, TopicSerializer, TypeOfAbilitySerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.db.models import Count, Sum
from django.utils import timezone
import csv


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

    #db_response = Answers.objects.select_related('ability')#.values('ability', 'n_times_reviewed', 'answers')
    #db_response = Answers.objects.select_related('ability')#.values('ability', 'n_times_reviewed', 'answers')
    #db_response = Ability.objects.filter(topic=2)#.filter(id=2)#.values('ability', 'n_times_reviewed', 'answers')
    #db_response = Ability.objects.filter(id__lte=12)#.filter(id=2)#.values('ability', 'n_times_reviewed', 'answers')
    #db_response = Ability.objects.all()#.filter(id=2)#.values('ability', 'n_times_reviewed', 'answers')
    #db_response = Ability.objects.filter(topic=5)#.filter(id=2)#.values('ability', 'n_times_reviewed', 'answers')
    #random_indexes = choose_abilities1(100)
    #if id_topic is not None:
        
     #   db_response = Ability.objects.filter(topic=id_topic, n_times_reviewed=0, id__in=random_indexes)#.filter(id=2)#.values('ability', 'n_times_reviewed', 'answers')
    #else:
        # print('except')
        #db_response = Ability.objects.filter(n_times_reviewed=0, id__in=random_indexes)#.filter(id=2)#.values('ability', 'n_times_reviewed', 'answers')
        #db_response = Ability.objects.all()#.filter(id=2)#.values('ability', 'n_times_reviewed', 'answers')
    topics = Topic.objects.all()
    print('random topic')
    print('topics')
    print(topics)
    print(len(topics))
    
    if True:
            #r = random.randint(1, len(topics))
            #random_topic = Topic(id=r)            
            #print('random_topic')
            #print(random_topic)
            # print('r')
            # print(r)
            # print('Topic.objects.get(id=r).topic')
            # topic = Topic.objects.get(id=r).topic
            # print(topic)
            # with open('api/csv_files/seen_topics.csv', 'a') as f:
            #     writer = csv.writer(f)
            #     writer.writerow(
            #         [topic,str(r)],
            #     )
                
            # #     print('reader')
            # f.close()
            excluded_topics = []
            if len(topics) > 1:
                
                with open('api/csv_files/seen_topics.csv', newline='') as f:
                    reader = csv.reader(f)
                    print('rows')
                    for row in reader:
                        try:
                            print(int(row[-1]))
                            excluded_topics.append(int(row[-1]))
                        except:
                            pass
                f.close()
            print('excluded_topics')
            print(excluded_topics)
            #excluded_topics = [x for x in range(1, 38) if x!=18]
            if len(topics) == len(excluded_topics):
                print('ENTERED?')
                with open('api/csv_files/seen_topics.csv', 'w+', newline='') as f:
                    writer = csv.writer(f)
                    
                f.close()
                excluded_topics = []

            print(excluded_topics)
            random_topics = Topic.objects.exclude(id__in=excluded_topics)
            print('random_topics')
            print(random_topics)
            r = random.randint(len(random_topics))
            topic_choosen = random_topics[r]
            print('topic_choosen')
            print(topic_choosen)
            print('sirve id?')
            print(topic_choosen.id)
            print(type(topic_choosen.id))
            id = topic_choosen.id
            with open('api/csv_files/seen_topics.csv', 'a') as f:
                writer = csv.writer(f)
                #topic = Topic.objects.get(id=id).topic
                writer.writerow(
                    [topic_choosen,str(id)],
                )
                
            #     print('reader')
            f.close()

           
            
        #random_topic = Topic(id=1)
        #random_topic = Topic(id=random.randint(1, len(topics)))
        # day_of_month = int(str(timezone.now().date())[-2:])
        # if day_of_month <= 7:
        #     random_topic = Topic(id=1)
        # elif 23 <= day_of_month:
        #     random_topic = Topic(id=random.randint(len(topics)))
       
    
        #print(random_topic)
    db_response = Ability.objects.filter(topic=topic_choosen).order_by('n_times_reviewed', '-created_at__date')[:50]
    #print(type(db_response))
    #for ability in db_response:
        
     #   print(ability, ability.n_times_reviewed)
    #print(type(QuerySet(list(db_response))))
    #print(list(db_response))
    #print('respuesta')
    #print(type(db_response[0]))
    #print(db_response.answers_set.all())
    # print(db_response[0])
    # print(db_response[0].ability.ability)
    # print(db_response[0].ability.n_times_reviewed)
    # print(db_response[0].answer)
    # print(type(db_response[0]))
    #print(db_response.ability)
    #print('tipo de datito')
    #print(type(db_response))
    #print(help(AbilitySerializer))
    serialized = AbilitySerializer(db_response, many=True)
    # print('type of serialized.data')
    # print(type(serialized))
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
    print('LLEEEGOOOOOO!!!!')
    print(request.data)
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
        ability.difficulty = request.data['difficulty']
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
    return Response({'success':'true'})