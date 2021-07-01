from django.urls import path


from .views import PostListView, PostDetailView, PostCreateView, SearchResultsListView, CatDetailView, CatListView

app_name = 'phitube'

urlpatterns = [
    path('', PostListView.as_view(), name='media_list'),
    path('cat', CatListView.as_view(), name='cat_list'),
    path('post_create', PostCreateView.as_view(), name='media_create'),
    path('<uuid:pk>', PostDetailView.as_view(), name='media_detail'),
    path('cat/<int:pk>', CatDetailView.as_view(), name='cat_detail'),
    path('search/', SearchResultsListView.as_view(), name='media_results')

]
