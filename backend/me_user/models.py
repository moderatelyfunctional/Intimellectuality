from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from me_user.managers import MeUserManager

# Create your models here.
class MeUser(AbstractBaseUser, PermissionsMixin):
	username = models.CharField(_('username'), max_length=32, unique=True, db_index=True)
	description = models.TextField(_('body'), default='Don\'t leave this description desserted')

	objects = MeUserManager()

	USERNAME_FIELD = 'username'
