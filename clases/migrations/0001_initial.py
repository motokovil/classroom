# Generated by Django 2.2.14 on 2020-11-20 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('estudiantes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField(max_length=250)),
                ('estudiante', models.ManyToManyField(related_name='clase', to='estudiantes.Estudiante')),
            ],
        ),
    ]
