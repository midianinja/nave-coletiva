# Generated by Django 2.2.7 on 2019-11-17 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nave', '0005_espaco_eventos_simultaneos'),
    ]

    operations = [
        migrations.AddField(
            model_name='espaco',
            name='ordem',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
