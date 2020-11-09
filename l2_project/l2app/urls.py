from django.conf.urls import url
from l2app import views

urlpatterns = [
    url('',views.users,name = 'users')
]
