# Generated by Django 4.1.2 on 2022-12-07 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='funcionarios',
            fields=[
                ('id_funcionarios', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=100)),
                ('dataNascimento', models.CharField(max_length=100)),
                ('salario', models.CharField(max_length=100)),
                ('horas', models.CharField(max_length=100)),
                ('funcao', models.CharField(max_length=100)),
            ],
        ),
    ]