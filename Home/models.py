from django.db import models

# Create your models here.

class Monday(models.Model):
    time = models.TimeField()
    task = models.CharField(max_length=150)

class Tuesday(models.Model):
    time = models.TimeField()
    task = models.CharField(max_length=150)

class Wednesday(models.Model):
    time = models.TimeField()
    task = models.CharField(max_length=150)

class Thursday(models.Model):
    time = models.TimeField()
    task = models.CharField(max_length=150)

class Friday(models.Model):
    time = models.TimeField()
    task = models.CharField(max_length=150)

class Saturday(models.Model):
    time = models.TimeField()
    task = models.CharField(max_length=150)

class Sunday(models.Model):
    time = models.TimeField()
    task = models.CharField(max_length=150)
