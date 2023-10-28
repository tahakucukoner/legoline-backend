from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
import datetime


class MyUserManager(BaseUserManager):
    def create_user(self, username, tel_no, password=None):
        if not tel_no:
            raise ValueError("Users must have an tel_no address")

        user = self.model(
            tel_no=tel_no,
            username=username
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, tel_no, password=None):
        user = self.create_user(
            tel_no=tel_no,
            username=username
        )
        user.set_password(password)
        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)
        return


class CustomUser(AbstractBaseUser):
    name = models.CharField(blank=False, null=True, max_length=100)
    surname = models.CharField(blank=False, null=True, max_length=100)
    username = models.CharField(
        blank=False, null=True, max_length=100, unique=True)
    tel_no = models.CharField(blank=False, null=True, max_length=100,unique=True)
    email = models.EmailField(blank=True, null=True, unique=True)
    birthday = models.DateField(blank=True, null=True)
    gender = models.CharField(blank=False, max_length=10)
    created_at = models.DateTimeField(
        verbose_name="created at", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="update at", auto_now=True)
    is_active = models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)
    is_admin=models.BooleanField(default=False)
    qr_code = models.CharField(blank=False, max_length=200)
    member_id = models.CharField(blank=False, max_length=10)


    objects = MyUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['tel_no']

    def __str__(self):
        return str(self.username)
    
    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True
