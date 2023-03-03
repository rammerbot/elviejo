# Generated by Django 4.1.6 on 2023-02-28 16:13

from django.db import migrations, models
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('full_name', models.CharField(max_length=60, verbose_name='Nombre')),
                ('email', models.EmailField(max_length=254, verbose_name='Correo')),
                ('message', models.TextField(verbose_name='Mensaje')),
            ],
            options={
                'verbose_name': 'Contacto',
                'verbose_name_plural': 'Contactos',
            },
        ),
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20, verbose_name='Titulo')),
                ('description', models.TextField(verbose_name='Descripcion')),
                ('about_title', models.CharField(max_length=50, verbose_name='Titutlo nosotros')),
                ('about_text', models.TextField()),
                ('email_contact', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Correo de contacto')),
                ('phone', models.CharField(max_length=20, verbose_name='Telefono de contacto')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creacion')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='Fecha de Actualizacion')),
            ],
            options={
                'verbose_name': 'Pagina principal',
                'verbose_name_plural': 'Paginas principales',
            },
        ),
        migrations.CreateModel(
            name='Suscribers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, verbose_name='Correo')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creacion')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='Fecha de Actualizacion')),
            ],
            options={
                'verbose_name': 'Suscriptor',
                'verbose_name_plural': 'Suscriptores',
            },
        ),
    ]
