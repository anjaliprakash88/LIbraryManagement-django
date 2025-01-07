from django.urls import path,re_path
from . import views

urlpatterns = [
    
    path('',views.login,name='login'),
    path('register/',views.register,name='register'),

    path('home',views.home,name='home'),
    

    path('issue',views.issue,name='issue'),
    path('return_item',views.return_item,name='return_item'),
    path('history',views.history,name='history'),


    path('libhome', views.libhome, name="libhome"),
    re_path('librarian',views.librarian,name='librarian'),
    path('add-book/', views.addbookview),
    path('add-book/add', views.addbook),
    path('edit-book/', views.editbookview),
    path('edit-book/edit', views.editbook),
    path('delete-book/', views.deletebookview),

    path('logout',views.logout,name='logout')
]
