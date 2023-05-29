from django.shortcuts import render
from django.core.mail import send_mail
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect

from django.views.generic import CreateView, View
from django.views.generic.edit import FormView

from .forms import UserRegisterForm , LoginForm, UpdatePasswordForm, VerificationForm
from .models import User
from .functions import *


# Create your views here.

class UserRegisterView(FormView):
    template_name = 'users/register.html'
    form_class = UserRegisterForm
    success_url = '/'

    def form_valid(self, form):
        ''''''
        #Generamos el código de verificacion
        codigo = code_generator()

        User.objects.create_user(
            form.cleaned_data['username'],
            form.cleaned_data['email'],
            form.cleaned_data['password1'],
            nombres = form.cleaned_data['nombres'],
            apellidos = form.cleaned_data['apellidos'],
            genero = form.cleaned_data['genero'],
            codregistro = codigo # Se asigna el código al registro
        )
        #Ahora se enviará el código del email del usuario
        asunto = 'Confirmación de Email'
        mensaje = 'Código de Verificación: ' + codigo
        email_remitente = 'planeacion.datos@ilpingenieria.com'
        #<asunto>, <mensaje>, <email_remitente>, [<>]
        send_mail(asunto, mensaje, email_remitente, [form.cleaned_data['email'],])
        # Una vez confirmado, redirigir pantalla de validación
        return HttpResponseRedirect(
            reverse(
                'users_app:user-verification'
            )
        )
    
class LoginUser (FormView):
    template_name = 'users/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('home_app:panel')
    def form_valid(self, form):
        user = authenticate( #usuario de base de datos siempre y cuando este autenticado y exista dentro de la base de datos
            username = form.cleaned_data['username'],
            password = form.cleaned_data['password']
        ) # hasta acá se ha verficado
        #para hacer el login, le pasa a todo el sistema la info de que x usuario esta actigo en el sistema
        login(self.request, user) #con esto ya hace el login
        return super(LoginUser, self).form_valid(form)
    
class LogoutUser(View):
    #El view no requiere de un template
    #Si se pueden escribir funciones básicas como el get y el post
    #En este caso, como se reciben datos, se intercepta la función get
    def get(self, request, *args, **kargs):
        logout(request)
        return HttpResponseRedirect(
            reverse(
                'users_app:user-login'
            )
        )

class UpdatePasswordView(LoginRequiredMixin, FormView):
    template_name = 'users/update.html'
    form_class = UpdatePasswordForm
    success_url = reverse_lazy('users_app:user-login')
    login_url = reverse_lazy('users_app:user-login')

    def form_valid(self, form):
        # Para recuperar un usuario que está activo en este momento
        usuario = self.request.user
        user = authenticate( #usuario de base de datos siempre y cuando este autenticado y exista dentro de la base de datos
            username = usuario.username,
            password = form.cleaned_data['password1']
        )

        if user:
            new_password = form.cleaned_data['password2']
            usuario.set_password(new_password)
            usuario.save()

        logout(self.request) # para que el usuario este obligado a volver a ingresar posterior al cambio de contraseña

        return super(UpdatePasswordView, self).form_valid(form)
    
class CodeVerificationView(FormView):
    template_name = 'users/verification.html'
    form_class = VerificationForm
    success_url = reverse_lazy('users_app:user-login')
    def form_valid(self, form):
        
        return super(CodeVerificationView, self).form_valid(form)