# Generated by Django 2.2.14 on 2020-11-20 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clases', '0005_auto_20201120_1724'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clase',
            name='created',
            field=models.DateTimeField(auto_created=True, auto_now_add=True, null=True),
        ),
    ]
