from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=200)
    data_post = models.DateField()
    discripton = models.TextField()

    def __str__(self):
        return self.title
