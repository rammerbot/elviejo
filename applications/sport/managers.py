from django.db import models


class LeagueManager(models.Manager):

    """Obtener Ligas a traves del Buscador"""
    def buscador_ligas(self, kword):
        return self.filter(league__icontains = kword, public =True).order_by("created")