from django.conf.urls import url
from base_app import views

app_name = 'base_app'

urlpatterns=[
    url(r'^home/$',views.index,name='index'),
    url(r'^register/$',views.register,name='register'),
    url(r'^user_login/$',views.user_login,name='user_login'),
    url(r'^logout_user/$', views.user_logout, name='user_logout'),
    url(r'^userdash/$',views.userdash,name='userdash'),
    url(r'^admins_login/$',views.admins_login,name='admins_login'),
    url(r'^adminspage/$',views.adminspage,name='adminspage'),

]
