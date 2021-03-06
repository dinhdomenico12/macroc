from django.urls import path, include
from . import views

urlpatterns = [
      path('', views.home, name='home'),
      path('home/',views.home, name='homepage' ),
      path('meals/', views.index,  name='index'),
      path('meals/create/', views.Macro_create.as_view(), name='macrocreate'),
      path('meals/create/goals', views.Goals_create.as_view(), name='goalscreate'),
      path('accounts/', include('django.contrib.auth.urls')),
      path('accounts/signup', views.signup, name='signup'),
      path('meals/<int:pk>/update/', views.Macroupdate.as_view(), name='macroupdate'),
      path('meals/<int:macro_id>/delete', views.macro_delete),

]