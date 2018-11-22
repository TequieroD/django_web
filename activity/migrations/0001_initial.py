# Generated by Django 2.1.3 on 2018-11-20 14:32

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='classSummaryModel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('action_name', models.CharField(max_length=200)),
                ('action_detail', models.TextField()),
                ('action_datetime', models.DateTimeField(auto_now=True)),
                ('enable', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'class_summary',
            },
        ),
        migrations.CreateModel(
            name='signUpModel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('user_id', models.CharField(max_length=200)),
                ('class_id', models.CharField(max_length=200)),
                ('signup_datetime', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'sign_up',
            },
        ),
    ]