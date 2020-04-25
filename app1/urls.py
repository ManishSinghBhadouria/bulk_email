from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('logout',views.logout,name='logout'),
    path('register',views.register,name='register'),
    path('validate',views.validate,name='validate'),
    path('sendmail',views.sendmail,name='sendmail'),
    path('attachments',views.attachments,name='attachments'),
    path('sendattachments',views.sendattachments,name='sendattachments'),
    ]