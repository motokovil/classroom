# Generated by Django 2.2.14 on 2020-11-20 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estudiantes', '0004_auto_20201120_1735'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estudiante',
            name='created',
            field=models.DateTimeField(auto_created=True, auto_now=True, null=True),
        ),
    ]