from django.views import static
from django.conf import settings
from django.conf.urls import *
from django.contrib import admin

from votefinder.main import urls as main_urls
from votefinder.vfauth import urls as auth_urls

admin.autodiscover()

urlpatterns = [
    url(r'^auth/', include(main_urls)),
    url(r'^admin/', admin.site.urls),
    url(r'', include(auth_urls)),
]

if settings.DEBUG:
    urlpatterns += [
        url(r'^static/(?P<path>.*)$', django.views.static.serve, {'document_root': settings.STATIC_ROOT}),
    ]
