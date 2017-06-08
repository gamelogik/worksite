from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.db import models


# Create your models here.


class Cvs(models.Model):
    name = models.TextField(default="")
    email = models.TextField(default="")
    motivation = models.TextField(default="")

    def __str__(self):
        return self.name

class Sector(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    description = models.TextField(default="")

    def __str__(self):
        return self.title


class Job(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    order = models.IntegerField(default=0)
    sector = models.ForeignKey(Sector)

    class Meta:
        abstract = True
        ordering = ['order', ]

    def __str__(self):
        return self.title


class Text(Job):
    content = models.TextField(blank=True, default="")

    def get_absolute_url(self):
        return reverse('sectors:text', kwargs={
            'sector_pk': self.sector_id,
            'job_pk': self.id
        })


class Quiz(Job):
    total_questions = models.IntegerField(default=4)

    class Meta:
        verbose_name_plural = "Quizzes"

    def get_absolute_url(self):
        return reverse('sectors:quiz', kwargs={
            'sector_pk': self.sector_id,
            'job_pk': self.id
        })


class Question(models.Model):
    quiz = models.ForeignKey(Quiz)
    order = models.IntegerField(default=0)
    prompt = models.TextField(default="")

    class Meta:
        ordering = ['order', ]

    def get_absolute_url(self):
        return self.quiz.get_absolute_url()

    def __str__(self):
        return self.prompt


class MultipleChoiceQuestion(Question):
    shuffle_answers = models.BooleanField(default=False)

class TrueFalseQuestion(Question):
    pass

class Answer(models.Model):
    question = models.ForeignKey(Question)
    order = models.IntegerField(default=0)
    text = models.CharField(max_length=250)
    correct = models.BooleanField(default=False)

    class Meta:
        ordering = ['order', ]

    def __str__(self):
        return self.text

