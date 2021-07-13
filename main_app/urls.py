from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/',views.about, name='about' ),
    path('meals/', views.index,  name='index'),
    path('meals/create/', views.Macro_create.as_view(), name='macrocreate'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup', views.signup, name='signup'),
]