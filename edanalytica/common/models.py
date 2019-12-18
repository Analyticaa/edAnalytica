from django.db import models
from django.contrib.auth.models import User

import uuid

class BaseModel(models.Model):
    pass

    class Meta:
        abstract = True

class UUIDModel(BaseModel):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True

class EdAnalyticaModel(UUIDModel):
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True, null=False)
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='created_by')
    modified_at = models.DateTimeField(auto_now=True, null=False)
    modified_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='modified_by')
    deleted_at = models.DateTimeField(null=True)

    class Meta:
        abstract = True
