from abstract.models import AbstractModel
from django.db import models
from django.utils.translation import gettext_lazy as _
from authentication.models import MyUser

# Create your models here.

class Blog(AbstractModel):
    title = models.CharField(blank=False, max_length=100
    ,help_text=_('title of the post'))
    content = models.TextField(blank=False,help_text=_('content of the post'))
    tags = models.TextField(blank=True,help_text=_('tags of the post'))
    owner = models.ForeignKey(MyUser,on_delete=models.CASCADE)