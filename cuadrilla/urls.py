from django.contrib.auth.decorators import login_required
from django.views.generic.detail import DetailView
from django.conf.urls import patterns, url
from cuadrilla.views import (
    BomberoCreate,
    BomberoUpdate,
    BomberoDelete,
    BomberoDetail,
    BomberoList
)

urlpatterns = patterns('',
                       url(r'^$', BomberoList.as_view(),
                           name='bombero_list'),
                       url(r'^add/$',
                           login_required(BomberoCreate.as_view()),
                           name='bombero_add'),
                       url(r'^(?P<pk>\d+)/$',
                           DetailView.as_view(model=BomberoDetail),
                           name='bombero_view'),
                       url(r'^(?P<pk>\d+)/delete/$',
                           login_required(BomberoDelete.as_view()),
                           name='bombero_delete'),
                       url(r'^(?P<pk>\d+)/update/$',
                           login_required(BomberoUpdate.as_view()),
                           name='bombero_update'),
                       )
