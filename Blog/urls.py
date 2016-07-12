"""Blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.contrib import auth
from blogApp import views as blog_views
from django.contrib.auth.views import login


urlpatterns = [
    url(r'^$',blog_views.getBlogs,name='blog_get_blogs'),
    url(r'^detail/(\d+)/$',blog_views.getDetail,name='blog_get_detail'),
    url(r'^members/$',blog_views.showMembers,name='blog_get_members'),
    url(r'^editor/$',blog_views.writeNewBlog,name='blog_write'),
    url(r'^register/$',blog_views.register,name='blog_register'),
    url(r'^video/$',blog_views.video,name='blog_video'),
    url(r'^info/$',blog_views.infoDisplay,name='info'),
    url(r'^login/$',blog_views.login,name='blog_login'),
    url(r'^logout/$',blog_views.logout,name='blog_logout'),
    url(r'^control/$',blog_views.control,name='blog_control'),
    url(r'^newinfo/$',blog_views.info,name='blog_newInfo'),
    url(r'^about/$',blog_views.about,name='about'),
    # url(r'^login/$', login, name='blog_login'),
    url(r'^admin/', admin.site.urls),
]
