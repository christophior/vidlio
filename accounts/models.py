from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _
from userena.models import UserenaBaseProfile
from embed_video.fields import EmbedVideoField


class Item(models.Model):
    video = EmbedVideoField()  # same like models.URLField()

class MyProfile(UserenaBaseProfile):
    user = models.OneToOneField(User,
                                unique=True,
                                verbose_name=_('user'),
                                related_name='my_profile')
    # videos = models.ManyToManyField(Item)
    # video = EmbedVideoField()
