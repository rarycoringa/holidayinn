# Generated by Django 2.2.5 on 2019-10-17 02:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Quartos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='Título')),
                ('description', models.TextField(max_length=200, verbose_name='Descrição')),
                ('price', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Preço')),
                ('peoples', models.DecimalField(decimal_places=0, max_digits=2, verbose_name='Capacidade de pessoas')),
                ('smoke', models.BooleanField(default=True, verbose_name='Permitido Fumar')),
            ],
            options={
                'verbose_name': 'Quarto',
                'verbose_name_plural': 'Quartos',
            },
        ),
    ]