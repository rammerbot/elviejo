from django.db import models
from model_utils.models import TimeStampedModel
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.


class SobreNosotros(TimeStampedModel):

    reference_title = models.CharField("Titulo de Temporada", max_length=50)
    who = RichTextUploadingField("Quienes somos")
    image_who = models.ImageField("Imagen Quienes somos", upload_to="vision")
    vision = RichTextUploadingField("Vision")
    image_vision = models.ImageField("Imagen Vision", upload_to="vision")
    mision = RichTextUploadingField("Mision")
    image_mision = models.ImageField("Imagen Mision", upload_to="vision")
    values = RichTextUploadingField("Valores")
    image_values = models.ImageField("Imagen Valores", upload_to="vision")
    public = models.BooleanField("Activo", default=True)

    class Meta:
        verbose_name = "Sobre Nosotros"

    def __str__(self):
        return self.reference_title