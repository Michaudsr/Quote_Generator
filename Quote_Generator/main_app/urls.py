from django.urls import path
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login, name='login')
]