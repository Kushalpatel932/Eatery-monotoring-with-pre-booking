# Generated by Django 2.1.5 on 2020-03-07 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meal', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='meal',
            name='detail',
            field=models.TextField(default=''),
        ),
    ]
