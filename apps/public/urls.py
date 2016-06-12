from django.conf.urls import url
from .views import *


urlpatterns = [
    url(r'^$', IndexPage.as_view(), name='index'),
]