"""test_templete3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

from django.conf.urls.static import static
from django.conf import settings
from app01 import views
from app02 import views as views02
from app03 import views as views03
from app04 import views as views04

from django.views.generic import TemplateView
from app01.forms import LoginForm

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', views.app01_view_index, name='app01_view_index'),
    url(r'^index.html', views02.app02_view_publications_index, name='app01_view_index'),
    url(r'^research.html', views.app01_view_research, name='app01_view_research'),
    url(r'^contacts.html', views.app01_view_contacts, name='app01_view_contacts'),
    url(r'^schedule.html', views.app01_view_schedule, name='app01_view_schedule'),

    url(r'^news.html', views02.app02_view_news, name='app02_view_news'),
    url(r'^board.html', views03.app03_view_board, name='app03_view_board'),
    url(r'^people_prof.html', views02.app02_view_people_prof, name='app02_view_people_prof'),
    url(r'^people_member.html', views02.app02_view_people_member, name='app02_view_people_member'),
    url(r'^people_alumni.html', views02.app02_view_people_alumni, name='app02_view_people_alumni'),
    url(r'^people_collab.html', views02.app02_view_people_collab, name='app02_view_people_collab'),
    url(r'^publications.html', views02.app02_view_publications, name='app02_view_publications'),
    url(r'^nanocore_viewer.html', views04.app04_view_nanocore, name='app04_view_nanocore'),
    url(r'^nanocore_view.html', views04.app04_view_nanocore_view, name='app04_view_nanocore_view'),

    url(r'^signup/$', 'app01.views.signup', name='signup'),
    url(r'^signup_ok/$', TemplateView.as_view(
        template_name='signup_ok.html'), name='signup_ok'),

    url(r'^login/$', 'django.contrib.auth.views.login',
        {'authentication_form': LoginForm}, name='login_url'),
    url(r'^logout/$', 'django.contrib.auth.views.logout',
        {'next_page': '/login/'}, name='logout_url'),

#    url(r'^accounts/login/', 'django.contrib.auth.views.login', name='login',
#        kwargs={'template_name': 'login.html',}),
#    url(r'^accounts/logout/', views.logout_view, name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
