from django.contrib import admin
from django.conf.urls import url, include
from rest_framework_swagger.views import get_swagger_view


api_v1_docs = get_swagger_view('Shiptrader API', url='/api/v1/', urlconf='api_v1.urls')


urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^api/v1/docs/$', api_v1_docs),
    url(r'^api/v1/', include('api_v1.urls')),
]
