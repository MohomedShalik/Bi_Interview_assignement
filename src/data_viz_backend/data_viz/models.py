from django.db import models

# Create your models here.


class School(models.Model):
    id = models.IntegerField(primary_key=True)
    school_name = models.CharField(max_length=len("Christ King Catholic School, Bass Hill"))

class Class(models.Model):
    id = models.IntegerField(primary_key=True)
    class_name = models.CharField(max_length=100)

class Assessment_Areas(models.Model):
    id = models.IntegerField(primary_key=True)
    assessment_area_name = models.CharField(max_length=100)

class Student(models.Model):
    id = models.IntegerField(primary_key=True)
    student_name = models.CharField(max_length=100)

class Answers(models.Model):
    id = models.IntegerField(primary_key=True)
    answer = models.CharField(max_length=100)

class Award(models.Model):
    id = models.IntegerField(primary_key=True)
    award_name = models.CharField(max_length=100)

class Subject(models.Model):
    id = models.IntegerField(primary_key=True)
    subject_name = models.CharField(max_length=100)

class Summary(models.Model):

    id = models.IntegerField(primary_key=True)
    school_id = models.IntegerField()
    student_id = models.IntegerField()
    class_id = models.IntegerField()
    subject_id = models.IntegerField()
    answer_id = models.IntegerField()
    assessment_area_id = models.IntegerField()
    correct_answer = models.CharField(max_length=100)
    correct_answer_id = models.IntegerField()
    sydney_participants = models.IntegerField()
    student_score = models.DecimalField(max_digits=10,decimal_places=3)
    participant = models.IntegerField() 
    correct_answer_percentage_per_class = models.DecimalField(max_digits=10,decimal_places=3)
    sydney_percentile = models.IntegerField()
    award_id = models.IntegerField()
    year_level_name = models.CharField(max_length=100)











