# Generated by Django 2.2.5 on 2019-10-15 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acomodacoes', '0002_auto_20191015_1827'),
    ]

    operations = [
        migrations.AddField(
            model_name='quartos',
            name='image',
            field=models.ImageField(blank=True, upload_to='static/images', verbose_name='Imagem'),
        ),
    ]