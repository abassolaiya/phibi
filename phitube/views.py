from django.shortcuts import render
from django.db.models import Q
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.edit import FormMixin
from django.urls import reverse
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Phitube, Category
from .forms import CommentForm, PhitubeForm

# Create your views here.
class PostListView(ListView):
    model = Phitube
    context_object_name = 'media_list'
    template_name = 'phitube/post_list.html'

class PostDetailView(FormMixin, DetailView):
    model = Phitube
    context_object_name = 'media_detail'
    pagination_by = 30
    template_name = 'phitube/post_detail.html'
    form_class = CommentForm

    def get_success_url(self):
        return reverse('phitube:media_detail', kwargs={'pk': self.object.id})

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Phitube
    template_name = 'phitube/post_create.html'
    fields = ('author', 'title', 'description', 'embeded_url','banner')
    success_url = reverse_lazy('phitube:media_list')
    login_url = 'account_login'

    def get_initial(self):
        return {
            'author': self.request.user.id
        }

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class SearchResultsListView(ListView): # new
    model = Phitube
    context_object_name = 'media_list'
    template_name = 'phitube/search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Post.objects.filter(Q(title__icontains=query) | Q(body__icontains=query))


class CatDetailView(FormMixin, DetailView):
    model = Category
    context_object_name = 'cat_detail'
    pagination_by = 30
    template_name = 'phitube/cat_detail.html'
    form_class = PhitubeForm

    def get_success_url(self):
        return reverse('phitube:cat_detail', kwargs={'pk': self.object.id})

    def get_context_data(self, **kwargs):
        context = super(CatDetailView, self).get_context_data(**kwargs)
        context['form'] = PhitubeForm(initial={'category': self.object})
        return context


class CatListView(ListView):
    model = Category
    context_object_name = 'cat_list'
    template_name = 'phitube/cat_list.html'
