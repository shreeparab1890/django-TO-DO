# Generated by Django 2.0.6 on 2018-06-06 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('desc', models.CharField(max_length=500)),
                ('status', models.BooleanField(default=False)),
            ],
        ),
    ]
