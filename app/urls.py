from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'app'
urlpatterns =[
    path('', views.index, name='index'),
    path('users/<int:pk>/', views.user_detail, name='user_detail'),
    path('photos/new/', views.up_photo, name='up_photo'),
    path('photos/<int:pk>/', views.photo_detail, name='photo_detail'),
    path('photos/<str:category>/', views.photos_category, name='photos_category'),
    path('photos/<int:pk>/delete/', views.delete_photo, name='delete_photo'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='app/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout')
]
