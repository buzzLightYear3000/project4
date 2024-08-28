from django.db import models

# Create your models here.
class Recipe(models.Model):
    recipename = models.CharField(max_length=100)
    cook = models.CharField(max_length=100)
    cuisine = models.ManyToManyField(
        'cuisines.Cuisine',
        related_name='cuisines'
    )
    instructions = models.TextField(max_length=1000)
    owner = models.ForeignKey(
        'jwt_auth.User',
        on_delete=models.CASCADE,
        related_name='recipes_created'
    )

    def __str__(self):
        return f'{self.recipename} - {self.cook} ({self.cuisine})'
