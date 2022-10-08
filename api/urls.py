from django.urls import path 
from . import views 

urlpatterns = [
    path('<int:id_topic>/', views.getData, name='index'),
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
    path('get-goals/', views.getGoals, name='get-goals')
    
]