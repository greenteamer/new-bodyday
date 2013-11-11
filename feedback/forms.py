# -*- coding: utf-8 -*-
from django import forms
from blog.models import Review

class ContactForm(forms.Form):
    subject = forms.CharField(label=u'Ваше имя', max_length=250)
    phone = forms.CharField(label=u'Ваш телефон', max_length=250)
    sender = forms.EmailField(label=u'Ваша почта', required=False)
    message = forms.CharField(label=u'Сообщение', max_length=500,widget=forms.Textarea(attrs={'rows': 5, 'cols': 50}))
    #response = forms.CharField(label=u'Response text', max_length=500,widget=forms.Textarea(attrs={'rows': 5, 'cols': 50}))
    # cc_myself = forms.BooleanField(required=False)


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('title', 'sender', 'review',)


# class Review(forms.ModelForm):
#     class Meta:
#         model = Review
