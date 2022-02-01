from django.db import models
from django_extensions.db.models import AutoSlugField

class Question(models.Model):
    question=models.TextField('Question')
    difficulty_level=models.CharField('Difficulty level',max_length=13,choices=[('Beginner','Beginner'),('Intermediate','Intermediate'),('Expert','Expert'),('Prodigy','Prodigy')])
    sample_input=models.TextField('Sample Input')
    sample_output=models.TextField('Sample Output')
    question_id=AutoSlugField(max_length=5,populate_from=['question','difficulty_level'],unique=True,primary_key=True)


class UserAnswer(models.Model):
    solution=models.TextField('Write your code here')
    output=models.TextField('Your output',blank=True)
    question=models.ForeignKey(Question,on_delete=models.SET_NULL,null=True)
    answer_id=AutoSlugField(max_length=10,populate_from=['solution'],unique=True,primary_key=True)






