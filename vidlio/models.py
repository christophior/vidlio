from django.db import models
from userena.models import UserenaBaseProfile

class UserProfile(UserenaBaseProfile):
    user = models.ForeignKey(User, unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)