from django.urls import path 
from . import views 

urlpatterns = [
    #path('<str:probability_scheduled_query>/', views.getData, name='index'),
    path('', views.getData, name='index'),
    path('topics/', views.getTopics, name='topics'),
    path('send/', views.getPostData, name='post-data'),
    path('sendAbility/', views.getPostAbility, name='post-ability'),
    path('metrics/<slug:metric>/', views.getMetric, name='total-abilities'),
    path('minimum-number-of-abilities-reviewed-today/', views.getMinimumNumberOfAbilitiesReviewedToday, name='minimum-number-of-abilities-reviewed-today'),
    path('abilities-reviewed-today/', views.getAbilitiesReviewedToday, name='abilities-reviewed-today'),
    path('abilities-by-topic/', views.getAbilitiesByTopic, name='abilities-by-topic'),
    path('types-of-abilities/', views.getTypesOfAbilities, name='types-of-abilities'),
    path('diary/', views.getDiaryData, name='get-diary-data'),
    path('goals/', views.postGoals, name='post-goals'),
    path('get-goals/', views.getGoals, name='get-goals'),
    path('post-in-diary/', views.postInDiary, name='post-in-diary'),
    path('add-topic/', views.addTopic, name='add-topic'),
    path('add-time-studied-topic/', views.addTimeStudiedTopic, name='add-time-studied-topic'),
    path('get-time-studied-topic/', views.getStudiedTimeToday, name='get-time-studied-topic'),
    path('update-time-studied-topic/<int:id>/', views.updateTimeStudyingTopic, name='update-time-studied-topic'),
    
]