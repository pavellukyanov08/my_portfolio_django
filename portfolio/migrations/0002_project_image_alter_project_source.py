# Generated by Django 4.2.4 on 2023-08-25 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='image',
            field=models.ImageField(null=True, upload_to='portfolio/uploads'),
        ),
        migrations.AlterField(
            model_name='project',
            name='source',
            field=models.FileField(upload_to='portfolio/uploads/source'),
        ),
    ]
