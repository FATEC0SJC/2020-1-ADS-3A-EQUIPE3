# Generated by Django 2.2 on 2020-07-09 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vagas', '0006_auto_20200709_1443'),
    ]

    operations = [
        migrations.AddField(
            model_name='vaga',
            name='beneficios',
            field=models.ManyToManyField(blank=True, to='vagas.Beneficio', verbose_name='Benefícios da Vaga'),
        ),
    ]
