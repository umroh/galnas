"""galnas URL Configuration

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
from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from  . import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^data-manager/', include('managerData.urls', namespace='data-manager')),
]+ static(settings.DATA_URL, document_root=settings.DATA_ROOT)\
              # + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG is False:   #if DEBUG is True it will be served automatically
    urlpatterns.append('',
            # url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
            url(r'^Data/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.DATA_ROOT}),
    )
