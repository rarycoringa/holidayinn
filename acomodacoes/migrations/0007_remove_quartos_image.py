# Generated by Django 2.2.5 on 2019-10-16 00:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('acomodacoes', '0006_auto_20191015_1858'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quartos',
            name='image',
        ),
    ]