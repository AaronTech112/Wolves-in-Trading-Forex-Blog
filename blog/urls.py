from . import views
from django.urls import path
from django.conf.urls import handler400, handler403, handler404, handler500



# handler400 = 'my_app.views.bad_request'
# handler403 = 'my_app.views.permission_denied'
# handler500 = 'my_app.views.server_error'

urlpatterns = [
    path( '', views.home, name='home'),
    path( 'authorhome', views.author_home, name='author_home'),
    path( 'single/<str:pk>/', views.single, name='single'),
    path('next', views.next_home, name='next'),
    path('next', views.next2, name='next2'),
    path('next', views.nextlast, name='next_last'),
    path('author', views.author, name='author'),
    path('contact', views.contact, name='contact'),
    path('about', views.about, name = 'about'),
    path('adminlogin', views.adminlogin, name='adminlogin'),
    path('adminpage', views.adminpage, name='adminpage'),
    path('uploadpost', views.uploadpost, name='uploadpost'),
    path('editpost/<str:pk>/', views.editpost, name='editpost'),
]