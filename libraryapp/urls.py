from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),

    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),

    path('issue',views.issue,name='issue'),
    path('return_item',views.return_item,name='return_item'),
    path('history',views.history,name='history'),

    path('logout',views.logout,name='logout')
]
