from django.conf.urls import url
from . import views

app_name='protest'

urlpatterns = [
    url(r'^profile/$', views.IndexViewProfile.as_view(), name='index_profile'),
    url(r'^profile/(?P<pk>[0-9]+)/$', views.DetailViewProfile.as_view(), name='detail_profile'),
    url(r'^post/$', views.IndexViewPost.as_view(), name='index_post'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.DetailViewPost.as_view(), name='detail_post'),

    #/protest/add
    url(r'^post/add$', views.PostCreate.as_view(), name='post-create'),

    #/protest/update/2
    url(r'^post/update/(?P<pk>[0-9]+)/$', views.PostUpdate.as_view(), name='post-update'),

    #/protest/2/delete
    url(r'^post/(?P<pk>[0-9]+)/delete/$', views.PostDelete.as_view(), name='post-delete'),

    url(r'^register/$', views.UserFormView.as_view(), name='register'),
]