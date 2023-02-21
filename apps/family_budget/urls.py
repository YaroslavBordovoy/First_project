from django.urls import path

from . import views

app_name = "family_budget"

urlpatterns = [
    path("", views.test_func, name="budget"),
]
