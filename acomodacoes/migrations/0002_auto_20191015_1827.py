# Generated by Django 2.2.5 on 2019-10-15 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acomodacoes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quartos',
            name='description',
            field=models.TextField(max_length=200, verbose_name='Descrição'),
        ),
        migrations.AlterField(
            model_name='quartos',
            name='peoples',
            field=models.DecimalField(decimal_places=0, max_digits=2, verbose_name='Capacidade de pessoas'),
        ),
        migrations.AlterField(
            model_name='quartos',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Preço'),
        ),
        migrations.AlterField(
            model_name='quartos',
            name='smoke',
            field=models.BooleanField(default=True, verbose_name='Permitido Fumar'),
        ),
        migrations.AlterField(
            model_name='quartos',
            name='title',
            field=models.CharField(max_length=30, verbose_name='Título'),
        ),
    ]