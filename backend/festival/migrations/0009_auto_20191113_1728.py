# Generated by Django 2.2.7 on 2019-11-13 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('festival', '0008_auto_20191113_1720'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atividade',
            name='fim',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='atividade',
            name='inicio',
            field=models.DateTimeField(blank=True, null=True, verbose_name='início'),
        ),
    ]
