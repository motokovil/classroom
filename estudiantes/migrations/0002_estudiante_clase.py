# Generated by Django 2.2.14 on 2020-11-20 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clases', '0002_auto_20201120_1407'),
        ('estudiantes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='estudiante',
            name='clase',
            field=models.ManyToManyField(related_name='estudiante', to='clases.Clase'),
        ),
    ]
