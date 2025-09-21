from django.urls import path

from .views import WeblogListView, WeblogDetailView, weblogs_by_tag, search

urlpatterns = [
    path('', WeblogListView.as_view(), name="weblog_list"),
    path('<int:pk>/', WeblogDetailView.as_view(), name="weblog_detail"),
    path('tag/<int:tag_id>/', weblogs_by_tag, name="weblogs_by_tag"), 
    path('search/', search, name="search")
]
