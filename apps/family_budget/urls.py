from django.urls import path

from . import views

app_name = "family_budget"

urlpatterns = [
    path("", views.family_budget, name="budget"),
    path("creating-a-report/", views.create_post, name="create_post"),
    path("post-search/", views.search_post, name="search_post"),
    path("post-information/", views.read_post, name="post_information"),
]
