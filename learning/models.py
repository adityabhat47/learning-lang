from django.db import models

# Create your models here.



class languages(models.Model):
    # song title
    title = models.CharField(max_length=255, null=False)
    # name of complexity
    complexity = models.CharField(max_length=255, null=False)

    def __str__(self):
        return "{} - {}".format(self.title, self.complexity)