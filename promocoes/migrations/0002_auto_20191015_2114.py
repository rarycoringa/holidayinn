# Generated by Django 2.2.5 on 2019-10-16 00:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('promocoes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='promocoes',
            name='description',
            field=models.TextField(max_length=200, verbose_name='Descrição'),
        ),
        migrations.AlterField(
            model_name='promocoes',
            name='title',
            field=models.CharField(max_length=30, verbose_name='Título'),
        ),
    ]