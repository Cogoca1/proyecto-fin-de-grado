# Generated by Django 5.0.4 on 2024-04-12 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cvs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='experiencia',
            name='descripcion',
            field=models.CharField(default='', max_length=400),
        ),
    ]
