# Generated by Django 3.0.7 on 2020-06-13 02:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seguranca', '0005_auto_20200612_2302'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='login',
            name='salt',
        ),
    ]
