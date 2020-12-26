from django.db import models
from django_mysql.models import EnumField

class Survey(models.Model):
    date = models.DateField()
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name} - {self.date}'

class Question(models.Model):
    TYPES = (
        ('t', 'Text'),
        ('a', 'Alternative'),
        ('o', "Order")
    )
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE, related_name='questions',)
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    type = EnumField(choices=TYPES)

    def __str__(self):
        return f'{self.survey.name} - {self.title}'

class Option(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='options')
    description = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.question.survey.name} - {self.question.title} - {self.description}'

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    option_id = models.IntegerField(null=True)
    options = models.CharField(max_length=255, null=True)
    body = models.CharField(max_length=50, null=True)