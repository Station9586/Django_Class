# Generated by Django 4.2.9 on 2024-05-02 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('_myform', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='birth',
            field=models.IntegerField(default=None),
        ),
    ]
