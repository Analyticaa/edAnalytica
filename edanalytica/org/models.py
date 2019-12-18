from django.db import models
from django.contrib.auth.models import User

from common.models import EdAnalyticaModel

class Org(EdAnalyticaModel):
    name = models.CharField(max_length=250, null=False, blank=False)
    description = models.TextField(null=True, blank=True)
    logo = models.ImageField(null=False)
    users = models.ManyToManyField(User)

    class Meta:
        pass
