#coding: utf-8
from django.db import models
from ckeditor.fields import RichTextField


"""модель специалистов"""
class Expert(models.Model):
    title = models.CharField(u'Имя', max_length=255)
    datetime = models.DateTimeField(u'Дата публикации')
    content = RichTextField(u'О специалисте')
    image = models.ImageField(u'Фото', upload_to='Expert_thumb')

    class Meta:
        verbose_name = ('Специалисты')
        verbose_name_plural = ('Специалист')
        ordering = ['title']

    def __unicode__(self):
        return self.title
    def get_absolute_url(self):
        return "/experts/%i/" % self.id


