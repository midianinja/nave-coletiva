# Generated by Django 2.2.7 on 2019-11-09 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rede', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pessoa',
            name='redes',
            field=models.ManyToManyField(to='rede.Rede'),
        ),
    ]
