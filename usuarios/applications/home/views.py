from datetime import datetime
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.edit import FormView

#Vamos a construir nuestro propio Mixin

class FechaMixin(object):
    '''Imaginemos que en cada una de nuestas vistas como contexto necesitamos enviar una fecha'''
    def get_context_data(self, **kwargs):
        context = super(FechaMixin, self).get_context_data(**kwargs)
        context['fecha'] = datetime.now()
        return context
    


#=========================================================================================
class HomePage(LoginRequiredMixin, FechaMixin,TemplateView):
    template_name = 'home/index.html'
    login_url = reverse_lazy('users_app:user-login') # Atributo requerido para LoginRequiredMixin



    
class TemplatePruebaMixin(FechaMixin, TemplateView):
    template_name = 'home/mixin.html'