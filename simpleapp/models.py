from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.

class Post(models.Model):
    title = models.CharField(verbose_name=_('Название'), max_length=50)
    content = models.TextField(verbose_name=_('Содержание'),blank=True)

    class Meta:
        verbose_name = _('Пост')
        verbose_name_plural = _('Посты')
        ordering = ('title',)