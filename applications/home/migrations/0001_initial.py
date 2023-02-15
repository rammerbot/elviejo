# Generated by Django 4.1.6 on 2023-02-14 17:24

from django.db import migrations, models
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('title', models.CharField(max_length=20, verbose_name='Titulo')),
                ('description', models.TextField(verbose_name='Descripcion')),
                ('about_title', models.CharField(max_length=50, verbose_name='Titutlo nosotros')),
                ('about_text', models.TextField()),
                ('email_contact', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Correo de contacto')),
                ('phone', models.CharField(max_length=20, verbose_name='Telefono de contacto')),
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
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('email', models.EmailField(max_length=254, verbose_name='Correo')),
            ],
            options={
                'verbose_name': 'Suscriptor',
                'verbose_name_plural': 'Suscriptores',
            },
        ),
    ]
