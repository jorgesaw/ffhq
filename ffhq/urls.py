from django.conf.urls import patterns, include, url
from django.contrib import admin
from ffhq import views

urlpatterns = patterns('',
    url(r'^$', views.home, name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^about/', views.about, name='about'),
    url(r'^dashboard/', views.dashboard, name='dashboard'),
    url(r'^accounts/', include('allauth.urls')),
)
