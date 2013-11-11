#coding: utf-8
from django.db import models, settings

from django.contrib import admin
from PIL import Image
import os


"""модель для галереи"""
# Изменение (filename, URL) вставкой '.mini' и изменение расширения на jpg
def _add_mini(s):
    parts = s.split(".")
    parts.insert(-1, "mini")
    if parts[-1].lower() not in ['jpeg', 'jpg']:
        parts[-1] = 'jpg'
    return ".".join(parts)

# Удаление миниатюры с физического носителя.
def _del_mini(p):
    mini_path = _add_mini(p)
    if os.path.exists(mini_path):
        os.remove(mini_path)

# Основной класс модели галереи
class Photo(models.Model):
    title = models.CharField(max_length=250)
    image = models.ImageField(upload_to='gallery')
    captions = models.CharField(max_length=250, blank=True)

    class Meta:
        verbose_name = ('Иллюстрация')
        verbose_name_plural = ('Иллюстрации')
        ordering = ['title']

    def __unicode__(self):
        return self.title

# Добавляем к свойствам объектов модели путь к миниатюре
    def _get_mini_path(self):
        return _add_mini(self.image.path)
    mini_path = property(_get_mini_path)

# Добавляем к свойствам объектов модели урл миниатюры
    def _get_mini_url(self):
        return _add_mini(self.image.url)
    mini_url = property(_get_mini_url)

# Добавляем к свойствам объектов модели html код для отображения миниатюры
# Сделано в модели для упрощения вывода в админке. Смотрим далее.
    def get_mini_html(self):
        html = '<a class="fancybox" rel="gallery1" href="%s"><img src="%s" alt="%s"/></a>'
        return html % (self.image.url, _add_mini(self.image.url), self.captions)
    mini_html = property(get_mini_html)
    get_mini_html.short_description = ('Иллюстрация')
    get_mini_html.allow_tags = True

# Создаем свою save
# Добавляем:
# - создание миниатюры
# - удаление миниатюры и основного изображения
#   при попытке записи поверх существующей записи
    def save(self, force_insert=False, force_update=False, using=None):
        try:
            obj =  Photo.objects.get(id=self.id)
            if obj.image.path != self.image.path:
                _del_mini(obj.image.path)
                obj.image.delete()
        except:
            pass
        super(Photo, self).save()
        img = Image.open(self.image.path)
        img.thumbnail(
            (128, 128),
            Image.ANTIALIAS
        )
        img.save(self.mini_path, 'JPEG')

# Делаем свою delete с учетом миниатюры
    def delete(self, using=None):
        try:
            obj = Photo.objects.get(id=self.id)
            _del_mini(obj.image.path)
            obj.image.delete()
        except (Photo.DoesNotExist, ValueError):
            pass
        super(Photo, self).delete()

    def get_absolute_url(self):
        return ('photo_detail', None, {'object_id': self.id})

# Класс для админки с отображением миниатюры в листе изображений (get_mini_html)
# и возможностью физического, пакетного удаления
# изображений и миниатюр (full_delete_selected)
class PhotoAdmin(admin.ModelAdmin):
    admin.site.disable_action('delete_selected')
    def full_delete_selected(self, request, obj):
        for o in obj.all():
            o.delete()
    full_delete_selected.short_description = 'Удалить выбранные иллюстрации'
    actions = ['full_delete_selected']
    list_display = ('title', 'captions', 'get_mini_html')