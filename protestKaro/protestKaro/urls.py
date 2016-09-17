
from django.conf.urls import url, include
from django.contrib import admin
from protest import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('protest.urls')),
    url(r'^$', views.index_post, name='index_post'),


]
