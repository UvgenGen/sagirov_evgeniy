"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import include, url
from django.contrib import admin
from project.views import home
from person.views import curse_list, curse_info


urlpatterns = [
    url(r'^$', home),
    url(r'^person', include('person.urls')),
    url(r'^curse/$', curse_list),
    url(r'^curse/(?P<num>\d+)/$', curse_info),

    url(r'^admin/', admin.site.urls),

]