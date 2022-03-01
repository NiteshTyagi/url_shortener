from django.db import models
import uuid
from django.utils.translation import gettext_lazy as _

# Create your models here.

def _generate_uuid():
    uid = uuid.uuid4().int
    return uid

class URL(models.Model):

    id = models.CharField(_('URL ID'),max_length=50,primary_key=True, default=_generate_uuid, editable=False)
    long_url = models.URLField(max_length=1000,db_index=True,unique=True)
    short_url = models.URLField(max_length=100,db_index=True,editable=False)
    total_clicks = models.PositiveIntegerField(default=0,editable=False)
    created_at = models.DateTimeField(auto_now=True)


    def __str__(self) -> str:
        return self.short_url or ''

    class Meta:
        verbose_name_plural = _("URLs")