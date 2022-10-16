from django.db import models
import datetime 
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone

class Topic(models.Model):
   topic = models.CharField(max_length=200, unique=True)
   
   #father = models.ForeignKey('self', on_delete=models.DO_NOTHING)
   def __str__(self):
    return self.topic

class TypeOfAbility(models.Model):
    type = models.CharField(max_length=200)
    def __str__(self):
        return self.type
        
class Ability(models.Model):
    ability = models.TextField()
    n_times_reviewed = models.IntegerField(default=0)
    topic = models.ForeignKey(Topic, on_delete=models.RESTRICT, default=1)
    type = models.ForeignKey(TypeOfAbility, on_delete=models.RESTRICT, default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    difficulty = models.PositiveSmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)], default=5)
    answer_correctness = models.PositiveSmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)], null=True)
    last_presentation_at = models.DateTimeField(auto_now_add=True)
    days_to_present_again = models.PositiveSmallIntegerField(default=0)
    def __str__(self):
        return self.ability

class AfterWhenToReview(models.Model):
    ability = models.ForeignKey(Ability, on_delete=models.CASCADE)
    after_when_to_review = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.after_when_to_review

class Answers(models.Model):
    ability = models.ForeignKey(Ability, on_delete=models.CASCADE)
    answer = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, )
    def __str__(self):
        return self.answer

class Reviewed(models.Model):
    ability = models.ForeignKey(Ability, on_delete=models.DO_NOTHING)
    n_times_reviewed = models.IntegerField(default=0)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.ability.ability


class MinimumAbilitiesReviewedPerDay(models.Model):
    datetime = models.DateField(auto_now_add=True)
    minimum_abilities_reviewed_per_day = models.IntegerField(default=3)

class Diary(models.Model):
    description = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.description

class Goal(models.Model):
    goal = models.TextField()
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.goal


class ScheduleAbilities(models.Model):
    ability = models.ForeignKey(Ability, on_delete=models.CASCADE)
    presented_at = models.DateTimeField(auto_now_add=True)
    days_to_present_again = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return self.ability.ability

class ScheduleAbilitiesHistory(models.Model):
    ability = models.ForeignKey(Ability, on_delete=models.DO_NOTHING)
    presented_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.ability
    
    class Meta:
        get_latest_by = 'presented_at'

