# Generated by Django 3.0.3 on 2021-01-12 23:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('type', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='typeowner',
            name='priority',
            field=models.IntegerField(default=1),
        ),
    ]
