# Generated by Django 2.2.14 on 2020-11-20 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estudiantes', '0002_estudiante_clase'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estudiante',
            name='created',
            field=models.DateTimeField(auto_created=True, null=True),
        ),
    ]
