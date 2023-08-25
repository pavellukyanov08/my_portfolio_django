from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField(max_length=500)
    source = models.FileField(upload_to='portfolio/uploads/source')
    image = models.ImageField(upload_to='portfolio/uploads', null=True)

    def __str__(self):
        return self.title
