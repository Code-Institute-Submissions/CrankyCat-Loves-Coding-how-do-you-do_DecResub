from django.db import models

# Create your models here.
class AddFeeling(models.Model):

    FEELING_TYPES = [
        ('happy', 'Happy'),
        ('excited', 'Excited'),
        ('calm', 'Calm'),
        ('disppointed', 'Disppointed'),
        ('anxious', 'Anxious'),
        ('angry', 'Angry'),
    ]

    date = models.DateField(null=True)
    feelings = models.CharField(
        choices=FEELING_TYPES,
        null=True,
        max_length=15
    )
    details = models.TextField(null=True)

    def __str__(self):
        return self.feelings
