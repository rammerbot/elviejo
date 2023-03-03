from datetime import datetime, timedelta

from django.db import models
from model_utils.models import TimeStampedModel
from django.template.defaultfilters import slugify
from django.urls import reverse, reverse_lazy

from .managers import LeagueManager

# Create your models here.

class League(TimeStampedModel):

    league = models.CharField("Liga", max_length=50)
    front_page = models.ImageField("portada", upload_to='coutas')
    public = models.BooleanField("Avtivo", default=True)
    slug = models.SlugField(editable=False, max_length=300)
    objects = LeagueManager()

    class Meta:
        verbose_name = "Liga"
        verbose_name_plural = "Ligas"

    def __str__(self):
        return self.league
    
    """Generar slug unico"""
    def save(self, *args, **kwargs):
        now =  datetime.now()
        totaltime = timedelta(
            hours=now.hour,
            minutes=now.minute,
            seconds=now.second
        )
        seconds = int(totaltime.total_seconds())
        slug_unique = f'{self.league}{str(seconds)}'
        self.slug = slugify(slug_unique)
        super(League, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse_lazy('sport_app:sport_detail', kwargs = {
            'slug':self.slug
            })

class Quotes(TimeStampedModel):
    league = models.ForeignKey(League, on_delete=models.CASCADE)
    locals = models.CharField("Local", max_length=30)
    local_quote = models.DecimalField("Cuota del Local", max_digits=4, decimal_places=2)
    image_locals = models.ImageField("escudo Local", upload_to='coutas')
    visitors = models.CharField("Visitantes", max_length=30)
    visitor_quote = models.DecimalField("Cuota del Visitante", max_digits=4, decimal_places=2)
    image_visitors = models.ImageField("Escudo visitante", upload_to='coutas')

    class Meta:
        verbose_name = "Cuota"
        verbose_name_plural = "Cuotas"

    def __str__(self) -> str:
        return f"{self.locals} vs {self.visitors}"
    
    
    



    
