from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

class User(AbstractBaseUser):
  avatar = models.TextField(default="/media/avatars/default-avatar.png") 