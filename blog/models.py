#coding: utf-8
from django.db import models
from ckeditor.fields import RichTextField


"""модель статей блога"""
class Post(models.Model):
    title = models.CharField(max_length=255)
    datetime = models.DateTimeField(u'Дата публикации')
    content = RichTextField()
    image = models.ImageField(upload_to='Blog_thumb')
    main_post_choice = models.CharField(
        max_length=7,
        choices=(('notmain', 'нет'),
                 ('main', 'да'),),
        default='',)

    class Meta:
        verbose_name = ('Публикации')
        verbose_name_plural = ('Публикация')
        ordering = ['title']

    def post_in_main(self):
        return self.main_post_choice=='main'
    def __unicode__(self):
        return self.title
    def get_absolute_url(self):
        return "/blog/%i/" % self.id

"""модель статических страниц"""
class Page(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True)
    datetime = models.DateTimeField(u'Дата публикации')
    content = RichTextField()
    image = models.ImageField(upload_to='Page_thumb')

    class Meta:
        verbose_name = ('Страницы')
        verbose_name_plural = ('Страница')
        ordering = ['title']

    main_page_choice = models.CharField(
        max_length=7,
        choices=(('notmain', 'нет'),
                 ('main', 'да'),),
        default='')
    def page_in_main(self):
        return self.main_page_choice=='main'

    def __unicode__(self):
        return self.title
    def get_absolute_url(self):
        return "/page/%i" % self.id


"""модель отзывов"""
class Review(models.Model):
    datetime = models.DateTimeField(u'Дата публикации', auto_now=True)
    title = models.CharField(u'Имя', max_length=255)
    sender = models.EmailField(u'Почта')
    review = RichTextField()

    class Meta:
        verbose_name = ('Отзывы')
        verbose_name_plural = ('Отзыв')
        ordering = ['title']

    def __unicode__(self):
        return self.title
    review_choice = models.CharField(
        max_length=7,
        choices=(('dontposted', 'нет'),
                 ('posted', 'да'),),
        default='')

    def review_in_page(self):
        return self.review_choice == 'posted'

