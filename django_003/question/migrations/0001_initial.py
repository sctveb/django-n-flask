# Generated by Django 2.1.3 on 2018-11-14 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('answerA', models.CharField(max_length=500)),
                ('answerB', models.CharField(max_length=500)),
            ],
        ),
    ]
