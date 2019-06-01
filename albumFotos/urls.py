"""albumFotos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from fotos import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('album/', views.base, name='base'),
    path('admin/', admin.site.urls),
    path('album/category/', login_required(views.CategoryListView.as_view()), name='category-list'),
    path('album/category/<int:pk>/detail', login_required(views.CategoryDetailView.as_view()), name='category-detail'),
    path('album/photo/', login_required(views.PhotoListView.as_view()), name='photo-list'),
    path('album/photo/<int:pk>/detail', login_required(views.PhotoDetailView.as_view()), name='photo-detail'),
    #update
    path('album/photo/<int:pk>/update/', login_required(views.PhotoUpdate.as_view()), name='photo-update'),
    #create
    path('album/photo/create/', login_required(views.PhotoCreate.as_view()), name='photo-create'),
    #delete
    path('album/photo/<int:pk>/delete/', login_required(views.PhotoDelete.as_view()), name='photo-delete'),
    #login
    path('album/login', auth_views.LoginView.as_view(template_name='auth/login.html'), name='login'),
    #logout
    path('album/logout', auth_views.LogoutView.as_view(template_name='auth/logout.html'), name='logout'),
    #profile
    path('album/profile/<int:pk>', login_required(views.Profile.as_view(template_name='auth/profile.html')), name='profile'),
    #pwdchange
    path(
        'album/change-password/',
        login_required(auth_views.PasswordChangeView.as_view(template_name='auth/change-password.html')),
        name='password-change'
    ),
]
