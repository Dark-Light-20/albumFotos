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

urlpatterns = [
    path('album/', views.base, name='base'),
    path('admin/', admin.site.urls),
    path('album/category/', views.CategoryListView.as_view(), name='category-list'),
    path('album/category/<int:pk>/detail', views.CategoryDetailView.as_view(), name='category-detail'),
    path('album/photo/', views.PhotoListView.as_view(), name='photo-list'),
    path('album/photo/<int:pk>/detail', views.PhotoDetailView.as_view(), name='photo-detail'),
    #update
    path('album/photo/<int:pk>/update/', views.PhotoUpdate.as_view(), name='photo-update'),
    #create
    path('album/photo/create/', views.PhotoCreate.as_view(), name='photo-create'),
    #delete
    path('album/photo/<int:pk>/delete/', views.PhotoDelete.as_view(), name='photo-delete'),
]