from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from me_user.managers import MeUserManager

# Create your models here.
class MeUser(AbstractBaseUser, PermissionsMixin):
	username = models.CharField(_('username'), max_length=32, unique=True, db_index=True)
	description = models.TextField(_('body'), default='Don\'t leave this description desserted')

	objects = MeUserManager()

	USERNAME_FIELD = 'username'

class MeLink(models.Model):
	title = models.CharField(_('title'), max_length=255, blank=True)
	link = models.URLField(_('link'), max_length=200, blank=True)

class MePost(models.Model):
	title = models.CharField(_('title'), max_length=255, blank=True)
	author = models.ForeignKey(MeUser, on_delete=models.CASCADE)

	date_created = models.DateTimeField(_('date created'), default=timezone.now)
	links = models.ManyToManyField(MeLink, related_name='post_links')
