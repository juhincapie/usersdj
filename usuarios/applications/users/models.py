from django.db import models
from django.contrib.auth.models import AbstractBaseUser , PermissionsMixin
from .managers import UserManager

# Create your models here.

class User(AbstractBaseUser,PermissionsMixin ): # PermissionsMixin nos va ayudar a realizar control incluso de super usuarios
    '''Modelo para definir un usurio'''
    GENDER_CHOICES = (
        ('M', 'Masculino'),
        ('F', 'Femenido'),
        ('O', 'Otros')
    )
    username = models.CharField('Nombre de Usuario', max_length=15, unique=True)
    email = models.EmailField()
    nombres = models.CharField(max_length=30, blank=True)
    apellidos = models.CharField(max_length=30, blank=True)
    genero = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True)
    codregistro = models.CharField(max_length=6, blank=True ) #default='000000' ----> este se debe autogenerar
    #
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)#atributo que nos permite verificar si este usuario es verificado o no, ya existe dentro del abstractbaseuser

    USERNAME_FIELD = 'username'
    objects = UserManager()
    REQUIRED_FIELDS = ['email']

    def get_short_name(self):
        return self.username
    def get_full_name(self):
        return self.nombres + ' '+ self.apellidos