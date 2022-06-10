# Generated by Django 4.0.5 on 2022-06-07 04:41

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='todo_list',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField(blank=True)),
                ('created', models.DateField(default=datetime.datetime(2022, 6, 7, 4, 41, 54, 387563, tzinfo=utc))),
                ('category', models.ForeignKey(default='general', on_delete=django.db.models.deletion.CASCADE, to='todo_app.category')),
            ],
        ),
    ]
