# Generated by Django 2.2.7 on 2019-11-13 19:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('festival', '0009_auto_20191113_1728'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atividade',
            name='espaco',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='nave.Espaco', verbose_name='espaço'),
        ),
    ]
