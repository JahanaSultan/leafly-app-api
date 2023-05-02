from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.conf import settings

# Create your models here.


class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Email adresi vacibdir.')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True

        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True, verbose_name='Email adresi')
    name = models.CharField(max_length=255, verbose_name='Ad Soyad')
    is_active = models.BooleanField(default=True, verbose_name='Aktivdir')
    is_staff = models.BooleanField(default=False, verbose_name='İşçidir')

    objects = UserManager()

    USERNAME_FIELD = 'email'
    
    class Meta:
        verbose_name_plural = 'İstifadəçilər'
        verbose_name = 'İstifadəçi'



class Tea(models.Model):
    """Tea object"""
    name = models.CharField(max_length=255, verbose_name='Çayın adı')
    price = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Qiyməti')
    description = models.TextField(blank=True, verbose_name='Açıqlama')
    is_available = models.BooleanField(default=True, verbose_name='Mövcuddur')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Yaradılma tarixi')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Çaylar'
        verbose_name = 'Çay'
        ordering = ['-created_at']