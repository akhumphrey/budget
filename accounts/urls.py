from django.conf.urls import url

from . import views

app_name = 'accounts'
urlpatterns = [
  url(r'^(?P<pk>[0-9]+)/?$', views.DetailView.as_view(), name='detail'),
  url(r'^(?P<account_id>[0-9]+)/edit/?$', views.edit, name='edit'),
  url(r'^(?P<account_id>[0-9]+)/update/?$', views.update, name='update'),
  url(r'^new/?$', views.new, name='new'),
  url(r'^create/?$', views.create, name='create'),
  url(r'^create_transaction/?$', views.create_transaction, name='create_transaction'),
]
