# Generated by Django 4.1.6 on 2023-02-09 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatbot', '0003_message_message'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='direction',
        ),
        migrations.AddField(
            model_name='message',
            name='response',
            field=models.TextField(blank=True),
        ),
    ]
