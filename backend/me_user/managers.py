from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import BaseUserManager

class MeUserManager(BaseUserManager):
	def _create_user(self, username, password, is_superuser, **extra_fields):
		if not username:
			raise ValueError('The username must be set')
		if not password:
			raise ValueError('The password must be set')

		username = username.lower()
		user = self.model(username=username, is_superuser=is_superuser, **extra_fields)
		user.set_password(password)
		user.save(using=self._db)
		return user

	def try_fetch(self, *args, **kwargs):
		try:
			return self.get(*args, **kwargs)
		except ObjectDoesNotExist:
			return None

	def create_user(self, username, password, **extra_fields):
		return self._create_user(username, password, False, **extra_fields)

	def create_superuser(self, username, password, **extra_fields):
		return self._create_user(username, password, True, **extra_fields)

class MeLinkManager(BaseUserManager):
	def try_fetch(self, *args, **kwargs):
		try:
			return self.get(*args, **kwargs)
		except ObjectDoesNotExist:
			return None

class MePostManager(BaseUserManager):
	def try_fetch(self, *args, **kwargs):
		try:
			return self.get(*args, **kwargs)
		except ObjectDoesNotExist:
			return None
