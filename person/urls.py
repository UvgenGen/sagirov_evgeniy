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
from django.conf.urls import url
from person.views import Personlist, PersonDetailView, AddPerson, EditPerson, DeletePerson


urlpatterns = [
    url(r'(editperson/(?P<pk>\d+))/$', EditPerson.as_view(), name = 'edit_person'),
    url(r'(deleteperson/(?P<pk>\d+))/$', DeletePerson.as_view(), name = 'delete_person'),
    url(r'addperson/$', AddPerson.as_view(), name = 'addPerson'),
    url(r'(?P<pk>\d+)/$', PersonDetailView.as_view()),
    url(r'$', Personlist.as_view(), name = 'person'),
    
]
