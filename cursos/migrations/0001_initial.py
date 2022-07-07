# Generated by Django 4.0.6 on 2022-07-06 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=128, unique=True)),
                ('descricao', models.TextField()),
                ('autor', models.CharField(blank=True, default='EU', max_length=128, null=True)),
                ('ativo', models.BooleanField(default=True)),
            ],
        ),
    ]
