from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.archive),
    url(r'^create/', views.create_blogpost),
]
