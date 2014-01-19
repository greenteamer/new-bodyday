#coding: utf-8
from blog.models import Post, Page, Review
from gallery.models import Photo
from django.views.generic import ListView, DetailView
from django.views.generic.base import RedirectView
from django.shortcuts import get_object_or_404

from feedback.forms import ReviewForm
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.shortcuts import render

from feedback.forms import ContactForm, ShortForm
from django.core.mail import send_mail


class PostListView(ListView):
    context_object_name = 'last_posts'
    queryset = Post.objects.all()
    template_name = 'blog/list.html'

    def get_context_data(self, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)
        context['photo'] = Photo.objects.all()
        return context


class PostDetailView(DetailView):
    template_name = 'blog/detail.html'
    model = Post

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context['post_in_page'] = Post.objects.all()
        context['photo'] = Photo.objects.all()
        return context


class PageListView(ListView):
    context_object_name = 'page_context'
    queryset = Page.objects.all()
    template_name = 'blog/page.html'

    def get_context_data(self, **kwargs):
        context = super(PageListView, self).get_context_data(**kwargs)
        context['photo'] = Photo.objects.all()
        context['post'] = Post.objects.all()
        return context


class PageDetailView(DetailView):
    model = Page
    template_name = 'blog/pagedetail.html'

    def get_context_data(self, **kwargs):
        context = super(PageDetailView, self).get_context_data(**kwargs)
        context['post_in_page'] = Post.objects.all()
        context['photo'] = Photo.objects.all()
        return context






# массаж в москве
def vmoskve(request):
    if request.method == 'POST':
        form = ShortForm(request.POST)
        subject = u'bodyday заявка от %s' % request.POST['subject']
        message = u' %s \n телефон: %s' % (request.POST['subject'], request.POST['phone'])
        if form.is_valid(): # All validation rules pass
            send_mail(subject, message, 'teamer777@gmail.com', ['koryabins@mail.ru'], fail_silently=False)
            return HttpResponseRedirect('/') # Redirect after POST
    else:
        form = ShortForm()

    return render(request, 'blog/massazh-v-moskve.html', {
        'form': form,
    })






class ReviewListView(ListView):
    context_object_name = 'review_context'
    template_name = 'blog/review.html'
    queryset = Review.objects.all()

    def get_context_data(self, **kwargs):
        context = super(ReviewListView, self).get_context_data(**kwargs)
        context['post_in_page'] = Post.objects.all()
        context['photo'] = Photo.objects.all()
        return context


def addReview(request):
    form = ReviewForm(request.POST or None)
    if form.is_valid():
        review = form.save(commit=False)
        review.save()
        return HttpResponseRedirect('/thankyou2.html')
    else:
        form = ReviewForm()
    return render_to_response(
        'blog/add-review.html',
        {'form' : form },
        context_instance = RequestContext(request)
    )

def thankyou2(request):
    return render(request, 'blog/thankyou2.html')









