# Generated by Django 2.2.7 on 2019-11-13 01:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rede', '0005_auto_20191110_1653'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pessoa',
            name='redes',
            field=models.ManyToManyField(blank=True, to='rede.Rede'),
        ),
    ]
