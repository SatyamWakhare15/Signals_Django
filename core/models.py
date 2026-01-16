from django.db import models

# book model for testing signals
class Book(models.Model):
    title = models.CharField(max_length=100)
    
    def __str__(self):
        return self.title
