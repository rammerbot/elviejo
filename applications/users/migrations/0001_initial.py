# Generated by Django 4.1.7 on 2023-03-03 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(max_length=10, unique=True, verbose_name='Nombre de Usuario')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Correo')),
                ('nombre', models.CharField(blank=True, max_length=30, verbose_name='Nombre')),
                ('apellido', models.CharField(blank=True, max_length=30, verbose_name='Apellido')),
                ('ocupacion', models.CharField(blank=True, max_length=60, verbose_name='Ocupacion')),
                ('date_brth', models.DateField(blank=True, null=True, verbose_name='Fecha de nacimiento')),
                ('code_register', models.CharField(blank=True, max_length=6, verbose_name='Codigo de Registro')),
                ('gender', models.CharField(blank=True, choices=[('M', 'Masculino'), ('F', 'Femenino'), ('o', 'Otro')], max_length=1, verbose_name='Genero')),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
