from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    url(r'^sign_in/$', views.sign_in, name='sign_in'),
    url(r'^sign_up/$', views.sign_up, name='sign_up'),
    url(r'^sign_out/$', views.sign_out, name='sign_out'),
    path('profile/<int:user_pk>/', views.profile, name='profile'),
    path('profile/edit/<int:user_pk>/', views.edit, name='edit'),
    # path('profile/<int:user_pk>/change_pw/', views.change_pw, name='change_pw'),
]
