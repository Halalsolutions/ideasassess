# Generated by Django 5.1 on 2024-08-29 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('results', '0002_result_date_taken'),
    ]

    operations = [
        migrations.AddField(
            model_name='result',
            name='incorrect_answers',
            field=models.JSONField(default=dict),
        ),
    ]
