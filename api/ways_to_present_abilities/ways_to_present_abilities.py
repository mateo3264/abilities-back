from base.models import Topic, ScheduleAbilities, ScheduleAbilitiesHistory, Ability
import csv
from numpy import random
from django.utils import timezone 
from datetime import timedelta
import json 


#Esta función escoge al azar las habilidades a repasar
def get_abilities_at_random():
    print('RRAAAAAAAAAAAAAAANDOOOOOOOOOOOOOOOOOOOOMMMMM')
    all_abilities = sorted(Ability.objects.all(), key=lambda x:random.random())[:50]
    return all_abilities

#Esta función escoge un tópico al azar que no haya
# sido presentado. cuando todos se han presentado, se 
# empieza desde 0
def get_topics_at_random_with_memory():
            topics = Topic.objects.all()


            excluded_topics = []
            if len(topics) > 1:
                
                with open('api/csv_files/seen_topics.csv', newline='') as f:
                    reader = csv.reader(f)
                    
                    for row in reader:
                        try:
                            print(int(row[-1]))
                            excluded_topics.append(int(row[-1]))
                        except:
                            pass
                f.close()

            #excluded_topics = [x for x in range(1, 38) if x!=16]
            if len(topics) <= len(excluded_topics):
                with open('api/csv_files/seen_topics.csv', 'w+', newline='') as f:
                    writer = csv.writer(f)
                    
                f.close()
                excluded_topics = []

            #excluded_topics = [x for x in range(1, 41) if x!=33]
            random_topics = Topic.objects.exclude(id__in=excluded_topics)

            r = random.randint(len(random_topics))
            topic_choosen = random_topics[r]

            id = topic_choosen.id
            with open('api/csv_files/seen_topics.csv', 'a', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(
                    [topic_choosen,str(id)],
                )
            
            f.close()

            db_response = Ability.objects.filter(topic=topic_choosen).order_by('n_times_reviewed', '-created_at__date')[:50]

            return db_response

def string_to_list():
    with open('api/ways_to_present_abilities/fibonacci_sequence.txt') as f:
        fib_seq = f.read()
        fib_seq = fib_seq.split(',')
        fib_seq = [int(x) for x in fib_seq]
        return fib_seq



def get_abilities_by_schedule():
    fib_seq = string_to_list()
    
    sas = ScheduleAbilities.objects.all()
    now = timezone.now().date()
    ids_of_abilities_to_present = []
    for s in sas:
        schedule_for_ability = s.presented_at.date() + timedelta(s.days_to_present_again)
        schedule_for_ability = schedule_for_ability
        # print('now')
        # print(now)
        # print('schedule_for_ability')
        # print(schedule_for_ability)
        
        if  now >= schedule_for_ability:
            print(s.ability.id, s.id, s.ability, s.presented_at, s.days_to_present_again)
            ids_of_abilities_to_present.append(s.ability.id)
        
    abilities_to_present = Ability.objects.filter(id__in=ids_of_abilities_to_present).order_by('n_times_reviewed')

    abilities_to_schedule_history = []
    ##Añade a ScheduleAbilitiesHistory la habilidad presentada
    # try:
    #     last_id = ScheduleAbilitiesHistory.objects.latest()
    # except:
    #     last_id = 1
    # for a in abilities_to_present:
    #     abilities_to_schedule_history.append(ScheduleAbilitiesHistory(id=last_id, ability=a, presented_at=timezone.now()))
    #     last_id += 1
    
    # sash = ScheduleAbilitiesHistory.objects.bulk_create(abilities_to_schedule_history)
    return abilities_to_present

    # for a in ass:
    #     print(30*'*')
    #     print(a.ability, a.n_times_reviewed, a.difficulty, a.answer_correctness)

def get_abilities_by_schedule2(union=False):
    fib_seq = string_to_list()
    print('fib_seq')
    print(fib_seq)
    print(type(fib_seq))
    all_abilities = Ability.objects.all().order_by('-created_at', 'days_to_present_again')
    
    now = timezone.now()#.date()
    ids_of_abilities_to_present = []
    show_unanswered_questions = random.random() < 0.7
    for a in all_abilities:
        schedule_for_ability = a.last_presentation_at + timedelta(a.days_to_present_again)
        #schedule_for_ability = schedule_for_ability
        # print('now')
        # print(now)
        # print('schedule_for_ability')
        # print(schedule_for_ability)
        # if a.days_to_present_again == 1:
        #     print('miiireee')
        #     #print(a)
        #     print(a.id, a.ability, a.last_presentation_at, a.days_to_present_again)
        #     print('when is it scheduled?')
        #     print(a.last_presentation_at.date() + timedelta(a.days_to_present_again))

        if  now - timedelta(hours=6) >= schedule_for_ability:
            #print(30*'*')
            #print('a.answers_set.all()[0].answer')
            #print(a.answers_set.all()[0].answer)
            if not show_unanswered_questions:
                try:
                    algo = a.answers_set.all()[0].answer
                    #print(a.id, a.ability, a.last_presentation_at, a.days_to_present_again, a.answers_set.all()[0].answer)
                    ids_of_abilities_to_present.append(a.id)
                except:
                    pass
                    #print(30*'*')
                    #print(a.id, a.ability, a.last_presentation_at, a.days_to_present_again, a.answers_set.all())
            else:
                ids_of_abilities_to_present.append(a.id)

    
    if union:
        abilities_to_present = Ability.objects.filter(id__in=ids_of_abilities_to_present).order_by('-created_at', 'days_to_present_again')[:50//2]
        #TODO: Optimizar esta linea ('?' parece que es muy lento para big datasets)
        all_abilities_random =  Ability.objects.all().order_by('?')[0:25]
        abilities_to_present = abilities_to_present.union(all_abilities_random)

    else:
        abilities_to_present = Ability.objects.filter(id__in=ids_of_abilities_to_present).order_by('-created_at', 'days_to_present_again')[:50]
    #print(abilities_to_present)
    for a in abilities_to_present:
        print(a.id, a.ability, a.created_at, a.last_presentation_at)
    abilities_to_schedule_history = []
    ##Añade a ScheduleAbilitiesHistory la habilidad presentada
    # try:
    #     last_id = ScheduleAbilitiesHistory.objects.latest()
    # except:
    #     last_id = 1
    # for a in abilities_to_present:
    #     abilities_to_schedule_history.append(ScheduleAbilitiesHistory(id=last_id, ability=a, presented_at=timezone.now()))
    #     last_id += 1
    
    # sash = ScheduleAbilitiesHistory.objects.bulk_create(abilities_to_schedule_history)
    return abilities_to_present

    # for a in ass:
    #     print(30*'*')
    #     print(a.ability, a.n_times_reviewed, a.difficulty, a.answer_correctness)

  

    
    
    
    
    
    
    
    
    
    
    
    
    #if timezone.now().time() > datetime.datetime.strptime('20:00:00', '%H:%M:%S').time():
     #   pass

