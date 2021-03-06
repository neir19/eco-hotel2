# Generated by Django 3.1.7 on 2021-04-12 21:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TipoHabitacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('descripcion', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Habitacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(max_length=5)),
                ('estado', models.CharField(max_length=10)),
                ('costo', models.FloatField()),
                ('descripcion', models.TextField()),
                ('fkTipo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='habitacion.tipohabitacion')),
            ],
        ),
    ]
