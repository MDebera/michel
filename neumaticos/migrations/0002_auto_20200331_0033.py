# Generated by Django 3.0.3 on 2020-03-31 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('neumaticos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='neumatico',
            name='Historial',
            field=models.CharField(blank=True, default='Sin Cambios Aun', max_length=1000, null=True),
        ),
    ]