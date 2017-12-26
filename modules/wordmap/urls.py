from django.conf.urls import url
from rest_framework import routers

from . import views

urlpatterns = [
    url('^$', views.index, name='index')
]

router = routers.DefaultRouter()
router.register(r'words', views.WordViewSet, base_name='api_words')

urlpatterns += router.urls
