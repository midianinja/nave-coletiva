# Generated by Django 2.2.7 on 2019-11-10 16:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('festival', '0002_cria_categorias'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='encontro',
            options={'ordering': ('nome',)},
        ),
    ]
