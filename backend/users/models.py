from django.db import models

class UserProfile(models.Model):
    telegram_id = models.CharField(max_length=50, unique=True)
    nickname = models.CharField(max_length=50, unique=True)
    points = models.PositiveIntegerField(default=0)

class Tasks(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    points = models.PositiveIntegerField(default=0)



