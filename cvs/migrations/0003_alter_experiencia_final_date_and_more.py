# Generated by Django 5.0.4 on 2024-04-12 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cvs', '0002_experiencia_descripcion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experiencia',
            name='final_date',
            field=models.DateField(verbose_name='final trabajo'),
        ),
        migrations.AlterField(
            model_name='experiencia',
            name='inicio_date',
            field=models.DateField(verbose_name='inicio trabajo'),
        ),
    ]
