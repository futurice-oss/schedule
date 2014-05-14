from django.db import models
from django.contrib.auth.models import User


class FutuUser(models.Model):
    user = models.OneToOneField(User)
    supervisor = models.ForeignKey(User, related_name='supervisor_of',
            null=True)
