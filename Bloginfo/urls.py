from django.urls import path
from .views import BlogView 

urlpatterns = [
    path('/Blog_writer',BlogView.as_view(),name="BlogView"),
]
