# Generated by Django 3.0.7 on 2020-07-18 02:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('curso', '0001_initial'),
        ('disciplinas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='curso',
            name='disciplinas',
            field=models.ManyToManyField(to='disciplinas.Disciplina'),
        ),
    ]