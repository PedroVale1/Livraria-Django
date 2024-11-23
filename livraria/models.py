from django.db import models

class Book(models.Model):
  created_at = models.DateTimeField(auto_now_add=True)
  title = models.CharField(max_length=50)
  description = models.CharField(max_length=200)
  year = models.IntegerField()
  genre = models.CharField(max_length=30)
  value = models.FloatField()

  def __str__(self):
    return(f'{self.title}-{self.value}')
