# Generated by Django 3.0 on 2019-12-18 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0007_auto_20191218_0741'),
    ]

    operations = [
        migrations.AddField(
            model_name='submissions',
            name='is_correct',
            field=models.BooleanField(default=False),
        ),
    ]