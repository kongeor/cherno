from django.db import models

from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import User

from django.core.validators import MaxValueValidator, MinValueValidator 


class Evolution(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # Generic

    public = models.BooleanField(default=True)
    min_rating = models.IntegerField(blank=True)
    min_perc_rating = models.IntegerField(blank=True)

    # Evolution Params

    initial_iterations = models.IntegerField(default=0,
        validators=[MinValueValidator(0)])
    total_iterations = models.IntegerField(default=100,
        validators=[MinValueValidator(1)])

    crossover_rate = models.IntegerField(default=30,
        validators=[MinValueValidator(0), MaxValueValidator(100)])
    mutation_rate = models.IntegerField(default=1,
        validators=[MinValueValidator(0), MaxValueValidator(100)])

    # Music Params

    KEYS = [
        ('C', 'C'),
        ('C#', 'C#'),
    ]

    key = models.CharField(
        max_length=2,
        choices=KEYS,
        default='C',
    )

    PATTERN = [('I-IV-V-I', 'I-IV-V-I')]

    pattern = models.CharField(
        max_length=20,
        choices = PATTERN,
        default = 'I-IV-V-I'
    )

    tempo = models.IntegerField(default=60)

class Iteration(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    value = models.IntegerField()
    evolution = models.ForeignKey(Evolution, on_delete=models.CASCADE)

class Chromosome(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    iteration = models.ForeignKey(Iteration, on_delete=models.CASCADE)
    fitness = models.FloatField()
    genes = ArrayField(models.IntegerField())
    abc = models.TextField()

class Invitation(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    email = models.EmailField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    evolution = models.ForeignKey(Evolution, on_delete=models.CASCADE)

class Rating(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    chromosome = models.ForeignKey(Chromosome, on_delete=models.CASCADE)
    value = models.SmallIntegerField()
