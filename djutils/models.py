###############################################################################
## Import Python
###############################################################################
from datetime import datetime


###############################################################################
## Import Django
###############################################################################
from django.conf import settings
from django.db import models
from django.utils.timezone import now


###############################################################################
## Code
###############################################################################
def usetz_now():
    USE_TZ = getattr(settings, 'USE_TZ', False)
    if USE_TZ:
        return now()
    else:
        return datetime.utcnow()


###############################################################################
## Models
###############################################################################
class BaseModel(models.Model):
    """ This is an abstract base class for other classes. """
    created = models.DateTimeField(default=usetz_now, db_index=True)
    updated = models.DateTimeField(default=usetz_now, db_index=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.updated = usetz_now()
        super(BaseModel, self).save(*args, **kwargs)
