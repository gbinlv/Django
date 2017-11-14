from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^index$', views.index, name="index"),
    url(r'^keyboard/', views.keyboard, name="keyboard"),
    url(r'^player/', views.player, name="player"),
]
