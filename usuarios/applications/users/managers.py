from django.db import models

from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager, models.Manager):
    def _create_user(self, username, email, password,  is_staff, is_superuser, **extra_fields): # is_staff define si el usuario puede o no acceder al administrador de django, is_superuser define si el usuario que se está creando es o no un super usuario
        user = self.model(
            username = username,
            email = email,
            is_staff = is_staff, # Booleano
            is_superuser = is_superuser, # Booleano
            **extra_fields
        )
        user.set_password(password) # Encripta ese password
        user.save(using = self.db) #using hace referencia a que base de datos vamos a trabajar
        return user
    
    def create_user(self, username, email, password = None, **extra_fields):
        return self._create_user(username, email, password, False,  False, **extra_fields )

    def create_superuser(self, username, email, password = None, **extra_fields):
        return self._create_user(username, email, password, True, True, **extra_fields )  #Función privada, solo quiero que se acceda a ese create_superuser cuando llamen la función en específico o cuando la llame del terminal
    