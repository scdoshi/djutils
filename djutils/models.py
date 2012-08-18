###############################################################################
## Import Python
###############################################################################
from datetime import datetime


###############################################################################
## Import Django
###############################################################################
from django.db import models


###############################################################################
## Models
###############################################################################
class BaseModel(models.Model):
    """ This is an abstract base class for other classes. """
    created = models.DateTimeField(default=datetime.utcnow, db_index=True)
    updated = models.DateTimeField(default=datetime.utcnow, db_index=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.updated = datetime.utcnow()
        super(ViaModel, self).save(*args, **kwargs)
