from django.urls import path,include
from .import views
urlpatterns = [
    path('register', views.register,name='register'),
    path('login', views.login,name='login'),
    path('admn', views.admn,name='admn'),
    path('add', views.add,name='add'),
    path('delete/<int:id>', views.delete,name='delete'),
    path('edit/<int:id>', views.edit,name='edit'),
    path('logout', views.logout,name='logout'),
    
    
]