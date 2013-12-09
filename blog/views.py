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
    # context_object_name = 'page'
    model = Page
    template_name = 'blog/pagedetail.html'
    # queryset = Page.objects.all()

    def get_context_data(self, **kwargs):
        context = super(PageDetailView, self).get_context_data(**kwargs)
        context['post_in_page'] = Post.objects.all()
        context['photo'] = Photo.objects.all()
        return context


# redirect
# class PageRedirectView(RedirectView):
#     permanent = True
#     query_string = True
#     pattern_name = 'page'
#     # url = 'test'
#
#     def get_redirect_url(self, *args, **kwargs):
#         page = get_object_or_404(Page, pk=id())
#         page.slug()
#         return super(PageRedirectView, self).get_redirect_url(*args, **kwargs)


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









