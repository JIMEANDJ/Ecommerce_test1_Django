from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.

class Administrador_Cuentas(BaseUserManager):
    def create_user(self, nombre, apellido, username, email, password=None):
        if not email:
            raise ValueError("username debe tener correo electronico")
        if not username:
            raise ValueError("username debe tener un nombre de username")
        username= self.model(
            email=self.normalize_email(email),
            username = username,
            nombre = nombre,
            apellido = apellido,            
        )
        
        username.set_password(password)
        username.save(using=self._db)
        return username
    
    
    def create_superuser (self, nombre, apellido, email, username, password):
        username = self.create_user(
            email=self.normalize_email(email),
            username = username,
            password= password,  
            nombre = nombre, 	
            apellido = apellido,                      
        )
        username.is_admin = True
        username.is_active = True
        username.is_staff = True
        username.is_superadmin = True
        username.save(using = self._db)
        return username



class Cuenta(AbstractBaseUser):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    celular = models.CharField(max_length=50)

    fecha_registro = models.DateField(auto_now=True)
    ultimo_acceso = models.DateField(auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'nombre', 'apellido' ]


    objects = Administrador_Cuentas()

    def full_name(self):
        return f'{self.nombre} {self.apellido}'

    def __str__(self):
        return self.email
    
    def has_perm(self, perm, obj=None):
        return self.is_admin
    
    def has_module_perms(self, add_label):
        return True
