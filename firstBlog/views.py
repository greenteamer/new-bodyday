from blog.models import Post, Page
from gallery.models import Photo
from django.views.generic import ListView, DetailView

class HomeListView(ListView):
    context_object_name = 'last_posts'
    queryset = Post.objects.all()
    template_name = 'blog/home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeListView, self).get_context_data(**kwargs)
        context['photo_context'] = Photo.objects.all()
        context['page_context'] = Page.objects.all()
        # And so on for more models
        return context
