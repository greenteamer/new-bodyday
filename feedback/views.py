# -*- coding: utf-8 -*-

from feedback.forms import ContactForm
from django.core.mail import send_mail


from django.shortcuts import render
from django.http import HttpResponseRedirect


def contact(request):
    if request.method == 'POST': # If the form has been submitted...
        form = ContactForm(request.POST)
        subject = u'bodyday заявка от %s' % request.POST['subject']
        message = u'сообщение: %s \n %s \n телефон: %s \n почта: %s' % (request.POST['message'], request.POST['subject'], request.POST['phone'], request.POST['sender'])
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            # ...
            #send_mail(form.request.subject, form.request.message,'teamer777@gmail.com', form.request.sender, fail_silently=False)
            #send_mail('сабжект', 'сообщение','teamer777@gmail.com', 'отправитель', fail_silently=False)
            send_mail(subject, message,'teamer777@gmail.com', ['greenteamer@bk.ru'], fail_silently=False)
            return HttpResponseRedirect('/thankyou.html') # Redirect after POST
    else:
        form = ContactForm() # An unbound form

    return render(request, 'blog/index.html', {
        'form': form,
    })

def thankyou(request):
    return render(request, 'blog/thankyou.html')

