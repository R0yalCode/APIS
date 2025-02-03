# Generated by Django 5.1.4 on 2025-01-20 14:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Administrador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('revision', models.TextField()),
                ('control', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Alerta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mensaje', models.CharField(max_length=255)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('tipo', models.CharField(choices=[('bajo_stock', 'Bajo Stock'), ('vencimiento', 'Vencimiento')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Insumo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identificador', models.CharField(max_length=10, unique=True)),
                ('nombre', models.CharField(max_length=50)),
                ('cantidadDisponible', models.IntegerField(default=0)),
                ('unidadMedida', models.CharField(max_length=30)),
                ('nivelReorden', models.IntegerField()),
                ('precioUnitario', models.FloatField()),
                ('ubicacion', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Inventario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('almacenamiento', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cliente', models.CharField(max_length=255)),
                ('fecha', models.DateField()),
                ('estado', models.CharField(choices=[('pendiente', 'Pendiente'), ('completado', 'Completado'), ('cancelado', 'Cancelado')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('edad', models.IntegerField()),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('precio', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('direccion', models.CharField(max_length=255)),
                ('contacto', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ReporteBodega',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=100)),
                ('datos', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ReporteConsumo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('periodoInicio', models.DateField()),
                ('periodoFin', models.DateField()),
                ('datos', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('rol', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Operacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('entrada', 'Entrada'), ('salida', 'Salida')], max_length=10)),
                ('cantidad', models.IntegerField()),
                ('fechaRegistro', models.DateTimeField(auto_now_add=True)),
                ('observaciones', models.TextField(blank=True, null=True)),
                ('insumo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='operaciones', to='inventario.insumo')),
            ],
        ),
        migrations.CreateModel(
            name='Historial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.TextField()),
                ('operacion', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='inventario.operacion')),
            ],
        ),
    ]
