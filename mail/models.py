#coding: utf-8
from django.core.mail import EmailMultiAlternatives
from django.db import models
from ckeditor.fields import RichTextField
from django.template import Context
from django.template.loader import get_template
from firstBlog.settings import EMAIL_HOST_USER


def send_email_message(context, to):
    html = get_template('blog/mail.html')
    text = get_template('blog/mail.txt')
    subject, to = unicode(context['title']), unicode(to)
    html_content = html.render(context)
    text_content = text.render(context)
    email = EmailMultiAlternatives(subject, text_content, EMAIL_HOST_USER, [to])
    email.attach_alternative(html_content, "text/html")
    return email.send()

"""модель статических страниц"""
class Mail(models.Model):
    title = models.CharField(max_length=255)
    to = models.EmailField(max_length=150)
    content = RichTextField()

    class Meta:
        verbose_name = ('Email')
        verbose_name_plural = ('Email')
        ordering = ['title']

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        c = Context({
            'title': self.title,
            'content': self.content,
            })
        send_email_message(c, self.to)
        super(Mail, self).save(*args, **kwargs)

