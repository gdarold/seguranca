# Generated by Django 3.0.7 on 2020-07-18 02:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pessoa', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='tipo_Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=149)),
            ],
        ),
        migrations.AddField(
            model_name='person',
            name='funcao',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pessoa.tipo_Person'),
        ),
    ]
