# Generated by Django 3.0.3 on 2020-03-31 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('RUT', models.IntegerField(max_length=12, primary_key=True, serialize=False)),
                ('Nombre', models.CharField(max_length=10)),
                ('Razon_social', models.CharField(max_length=20)),
                ('Direccion', models.CharField(max_length=40)),
                ('Telefono', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Neumatico',
            fields=[
                ('Fuego', models.IntegerField(max_length=12, primary_key=True, serialize=False)),
                ('Profundidad', models.FloatField(max_length=40)),
                ('Marca', models.CharField(max_length=40)),
                ('Radio', models.CharField(max_length=40)),
                ('Talle', models.CharField(max_length=40)),
                ('Banda', models.CharField(max_length=40)),
                ('Empresa', models.IntegerField(max_length=12)),
                ('KM_Recientes', models.IntegerField(default=0)),
                ('Cambiar_En', models.IntegerField(default=0, null=True)),
                ('Alta', models.DateField(null=True)),
                ('Historial', models.CharField(blank=True, max_length=1000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Vehiculo',
            fields=[
                ('matricula', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('Cantidad_neumaticos', models.IntegerField(default=0)),
                ('marca', models.CharField(max_length=10)),
                ('modelo', models.CharField(max_length=10)),
                ('Tipo_vehiculo', models.CharField(max_length=10)),
                ('empresa', models.IntegerField(max_length=50)),
                ('posicion1', models.IntegerField(default=0)),
                ('posicion2', models.IntegerField(default=0)),
                ('posicion3', models.IntegerField(default=0)),
                ('posicion4', models.IntegerField(default=0)),
                ('posicion5', models.IntegerField(default=0)),
                ('posicion6', models.IntegerField(default=0)),
            ],
        ),
    ]
