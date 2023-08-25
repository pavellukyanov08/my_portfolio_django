from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    logo = models.ImageField(upload_to='blogs/images', null=True)
    img = models.ImageField(upload_to='blogs/images', null=True)
    date = models.DateField()

    def __str__(self):
        return self.title
