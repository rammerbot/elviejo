# Generated by Django 4.1.7 on 2023-03-03 17:36

import ckeditor_uploader.fields
from django.db import migrations, models
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SobreNosotros',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('reference_title', models.CharField(max_length=50, verbose_name='Titulo de Temporada')),
                ('who', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Quienes somos')),
                ('image_who', models.ImageField(upload_to='vision', verbose_name='Imagen Quienes somos')),
                ('vision', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Vision')),
                ('image_vision', models.ImageField(upload_to='vision', verbose_name='Imagen Vision')),
                ('mision', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Mision')),
                ('image_mision', models.ImageField(upload_to='vision', verbose_name='Imagen Mision')),
                ('values', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Valores')),
                ('image_values', models.ImageField(upload_to='vision', verbose_name='Imagen Valores')),
                ('public', models.BooleanField(default=True, verbose_name='Activo')),
            ],
            options={
                'verbose_name': 'Sobre Nosotros',
            },
        ),
    ]
