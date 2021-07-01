from django.urls import path


from .views import PostListView, PostDetailView, PostCreateView, SearchResultsListView

app_name='blog'

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('post_create', PostCreateView.as_view(), name='post_create'),
    path('<uuid:pk>', PostDetailView.as_view(), name='post_detail'),
    path('search/', SearchResultsListView.as_view(), name='search_results')
]
