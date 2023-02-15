# Generated by Django 4.1.6 on 2023-02-14 20:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('entrada', '0002_entry_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='tag',
            field=models.ManyToManyField(to='entrada.tag'),
        ),
        migrations.RemoveField(
            model_name='entry',
            name='category',
        ),
        migrations.AddField(
            model_name='entry',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='entrada.category'),
            preserve_default=False,
        ),
    ]
