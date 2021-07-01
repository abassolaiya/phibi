from django.shortcuts import render
from django.db.models import Q
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.edit import FormMixin
from django.urls import reverse
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Post
from .forms import CommentForm

# Create your views here.
class PostListView(ListView):
    model = Post
    context_object_name = 'post_list'
    template_name = 'post/post_list.html'

class PostDetailView(FormMixin, DetailView):
    model = Post
    context_object_name = 'post'
    pagination_by = 30
    template_name = 'post/post_detail.html'
    form_class = CommentForm

    def get_success_url(self):
        return reverse('blog:post_detail', kwargs={'pk': self.object.id})

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context['form'] = CommentForm(initial={'post': self.object})
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.save()
        return super(PostDetailView, self).form_valid(form)

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'post/post_create.html'
    fields = ('title', 'body', 'image')
    success_url = reverse_lazy('blog:post_list')
    login_url = 'account_login'

    def get_initial(self):
        return {
            'author': self.request.user.id
        }

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class SearchResultsListView(ListView): # new
    model = Post
    context_object_name = 'post_list'
    template_name = 'posts/search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Post.objects.filter(Q(title__icontains=query) | Q(body__icontains=query))
