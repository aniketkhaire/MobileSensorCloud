from django.conf.urls import url
from . import views

app_name = 'user'

urlpatterns = [

    url(r'^login$', views.UserLoginView.as_view(), name='login'),
    url(r'^register$', views.RegistrationView.as_view(), name='register'),
]
