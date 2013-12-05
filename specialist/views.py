#coding: utf-8
from specialist.models import Expert
from blog.models import Post
from django.views.generic import ListView, DetailView



class ExpertListView(ListView):
    context_object_name = 'all_experts'
    queryset = Expert.objects.all().order_by('-datetime')
    template_name = 'blog/expertlist.html'

    def get_context_data(self, **kwargs):
        context = super(ExpertListView, self).get_context_data(**kwargs)
        context['post'] = Post.objects.all()
        return context


class ExpertDetailView(DetailView):
    context_object_name = 'expert'
    queryset = Expert.objects.all()
    template_name = 'blog/expertdetail.html'

    def get_context_data(self, **kwargs):
        context = super(ExpertDetailView, self).get_context_data(**kwargs)
        context['post_in_page'] = Post.objects.all()
        return context
