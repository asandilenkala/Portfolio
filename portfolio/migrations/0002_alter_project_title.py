# Generated by Django 5.0.1 on 2024-08-03 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]
