from django.db import models
from django.contrib.postgres.fields import ArrayField
from datetime import datetime, timedelta
from django.template.defaultfilters import slugify
from django.conf import settings
from django.urls import reverse, reverse_lazy
from ckeditor_uploader.fields import RichTextUploadingField
from .managers import EntryManager, CategoriaManager


# Create your models here.

class Category(models.Model):
    """Categorias de entrada"""

    short_name = models.CharField('Nombre corto', max_length=15, unique=True)
    create_at = models.DateTimeField('Fecha de Creacion', auto_now_add=True)
    update_at = models.DateTimeField('Fecha de Actualizacion', auto_now=True)
    objects = CategoriaManager()

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.short_name

class Tag(models.Model):

    name = models.CharField('Nombre', max_length=30)
    create_at = models.DateTimeField('Fecha de Creacion', auto_now_add=True)
    update_at = models.DateTimeField('Fecha de Actualizacion', auto_now=True)


    class Meta:
        verbose_name = "Etiqueta"
        verbose_name_plural = "Etiquetas"

    def __str__(self):
        return self.name

class Entry(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag)
    title = models.CharField('Titulo', max_length=80)
    resume = models.TextField('Resumen')
    content = RichTextUploadingField('Contenido')
    public = models.BooleanField('Activo', default=False)
    image = models.ImageField('Imagen', upload_to='entry')
    portada = models.BooleanField(default=False)
    in_home = models.BooleanField(default=False)
    slug = models.SlugField(editable=False, max_length=300)
    create_at = models.DateTimeField('Fecha de Creacion', auto_now_add=True)
    update_at = models.DateTimeField('Fecha de Actualizacion', auto_now=True)
    objects = EntryManager()
    video = models.URLField()

    class Meta:
        verbose_name = 'Entrada'
        verbose_name_plural = 'Entradas'

    def __str__(self) -> str:
        return self.title

    """Generar slug unico"""
    def save(self, *args, **kwargs):
        now =  datetime.now()
        totaltime = timedelta(
            hours=now.hour,
            minutes=now.minute,
            seconds=now.second
        )
        seconds = int(totaltime.total_seconds())
        slug_unique = f'{self.title}{str(seconds)}'
        self.slug = slugify(slug_unique)
        super(Entry, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse_lazy('entrada_app:detail', kwargs = {
            'slug':self.slug
            })
