from django.conf.urls import url
from . import views

app_name='protest'

urlpatterns = [
    url(r'^profile/$', views.index_profile, name='index_profile'),
    url(r'^profile/(?P<profile_id>[0-9]+)/$', views.detail_profile, name='detail_profile'),
    url(r'^post/$', views.index_post, name='index_post'),
    url(r'^post/(?P<post_id>[0-9]+)/$', views.detail_post, name='detail_post')
]