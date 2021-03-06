# Generated by Django 2.2.7 on 2019-11-13 17:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('festival', '0007_auto_20191113_0203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atividade',
            name='convidados',
            field=models.ManyToManyField(blank=True, related_name='convidado_para', to='rede.Pessoa'),
        ),
        migrations.AlterField(
            model_name='atividade',
            name='descricao',
            field=models.TextField(verbose_name='descrição'),
        ),
        migrations.AlterField(
            model_name='atividade',
            name='espaco',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nave.Espaco', verbose_name='espaço'),
        ),
        migrations.AlterField(
            model_name='atividade',
            name='inicio',
            field=models.DateTimeField(verbose_name='início'),
        ),
        migrations.AlterField(
            model_name='atividade',
            name='observacoes',
            field=models.TextField(blank=True, verbose_name='observações'),
        ),
        migrations.AlterField(
            model_name='atividade',
            name='responsavel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='responsavel_por', to='rede.Pessoa', verbose_name='responsável'),
        ),
        migrations.AlterField(
            model_name='atividade',
            name='titulo',
            field=models.CharField(max_length=255, verbose_name='título'),
        ),
    ]
