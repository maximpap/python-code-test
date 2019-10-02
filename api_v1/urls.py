from rest_framework import routers
from django.conf.urls import url, include
from rest_framework.schemas import get_schema_view

from api_v1.views import (
    shiptrader
)


router = routers.DefaultRouter()

router.register(r'starship', shiptrader.StarshipViewset)
router.register(r'listing', shiptrader.ListingViewset)
router.register(r'store', shiptrader.MarketViewset)

schema = get_schema_view(title='Shiptrader API', version='1.0.0')


app_name = 'api_v1'
urlpatterns = [
    url(r'^schema/$', schema),
    url(r'', include(router.urls)),
]
