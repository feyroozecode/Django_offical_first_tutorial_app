from django.db import models

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

# Model choice question have a relation with question accorded by foreignKey, relation is deleted when
class Choice(models.Model):
    question = models.ForeignKey(Question, 
        on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    