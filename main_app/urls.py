from django.urls import path, include
from . import views

urlpatterns = [
path('meals/', views.index,  name='index'),
path('about/',views.about, name='about' ),
# path('meals/create/', views.create, name='create'),
path('accounts/', include('django.contrib.auth.urls')),
path('accounts/signup', views.signup, name='signup'),
]