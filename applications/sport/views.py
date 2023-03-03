from django.shortcuts import render

from django.views.generic import ListView, DetailView

from .models import Quotes, League

# Create your views here.


class SportView(ListView):
    template_name = "sport/sport_list.html"
    context_object_name = "ligas"
    paginate_by = 9


    def get_queryset(self): 
        kword = self.request.GET.get("kword","")
        resultado = League.objects.buscador_ligas(kword)
        return resultado


class SportDetail(DetailView):
    template_name = 'sport/sport_detail.html'
    model = League
    context_object_name = "league"

    
    def get_context_data(self, **kwargs):
        league_slug = self.kwargs.get("slug")
        context = super(SportDetail,self).get_context_data(**kwargs)
        context["quotes"] = Quotes.objects.filter(league__slug=league_slug)
        
        return context
    
    
