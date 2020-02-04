from django.db import models
from django.contrib.auth.models import User

from common.models import EdAnalyticaModel

class Org(EdAnalyticaModel):
    org_id = models.CharField(max_length=10, null=False, unique=True)
    name = models.CharField(max_length=250, null=False, blank=False)
    description = models.TextField(null=True, blank=True)
    logo = models.ImageField(null=False)
    users = models.ManyToManyField(User)
    footer = models.TextField(max_length=500, null=False)

    def __str__(self):
        return "{}-{}".format(self.org_id, self.name)

    class Meta:
        pass
