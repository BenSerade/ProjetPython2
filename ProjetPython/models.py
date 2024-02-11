from django.db import models
from django.contrib.auth.models import User

class Session(models.Model):
    STATUS_CHOICES = (
        ('open', 'Ouvert'),
        ('closed', 'Fermé'),
    )
    form_status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='closed')
    opening_time = models.DateTimeField()
    closing_time = models.DateTimeField()

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    progress_percentage = models.DecimalField(max_digits=5, decimal_places=2)
    difficulty_level = models.CharField(max_length=20)
    personal_progress = models.CharField(max_length=50)

class FormSubmission(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    progress_percentage = models.DecimalField(max_digits=5, decimal_places=2)
    difficulty_level = models.CharField(max_length=20)
    personal_progress = models.CharField(max_length=50)
    submission_time = models.DateTimeField(auto_now_add=True)

class FormFirstLogin(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    first_login_time = models.DateTimeField(auto_now_add=True)
    some_field = models.CharField(max_length=20)
