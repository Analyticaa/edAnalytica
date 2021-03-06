# Generated by Django 3.0 on 2019-12-13 05:50

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='QuestionPool',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField(max_length=4000)),
                ('tags', models.CharField(blank=True, max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='QuestionType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('description', models.TextField(blank=True, null=True)),
                ('start_date', models.DateTimeField(auto_now_add=True)),
                ('end_date', models.DateTimeField()),
                ('questions', models.ManyToManyField(to='quiz.QuestionPool')),
            ],
        ),
        migrations.AddField(
            model_name='questionpool',
            name='question_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='quiz.QuestionType'),
        ),
        migrations.CreateModel(
            name='QuestionOptions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('options', models.TextField(max_length=4000)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='quiz.QuestionPool')),
            ],
        ),
    ]
