from django.db import models
from django.utils import timezone

class AbstractModel(models.Model):
    created     = models.DateTimeField(editable=False)
    modified    = models.DateTimeField()
    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(AbstractModel, self).save(*args, **kwargs)
    class Meta:
        abstract=True
        ordering=('-created',)