# Generated by Django 3.2.16 on 2023-01-03 23:52

from django.db import migrations, models
import plato.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Plato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(max_length=15, verbose_name='Color')),
                ('precio', models.DecimalField(decimal_places=2, default=9, max_digits=10, validators=[plato.validators.validar_precio], verbose_name='Precio')),
                ('campos', models.CharField(blank=True, max_length=20, null=True, verbose_name='Campos')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre del plato')),
                ('fecha_inicio', models.DateField()),
                ('oferta', models.CharField(choices=[('SI', 'SI'), ('NO', 'NO')], default='NO', max_length=2, verbose_name='Oferta')),
            ],
        ),
    ]