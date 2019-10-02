import coreapi
from rest_framework import viewsets, filters

from shiptrader import (
    models as shiptrader_models,
    serializers as shiptrader_serializers
)


class StarshipViewset(viewsets.ReadOnlyModelViewSet):
    queryset = shiptrader_models.Starship.objects.all()
    serializer_class = shiptrader_serializers.StarshipSerializer

    def list(self, request, *args, **kwargs):
        """
        Returns list of all known starships.

        ## 200 Response data

        Starships list

            {
              "count": int,
              "next": next page url,
              "previous": prev page url,
              "results": [
                {
                    "id": int,
                    "starship_class": string,
                    "manufacturer": string,
                    "length": float,
                    "hyperdrive_rating": float,
                    "cargo_capacity": int,
                    "crew": int,
                    "passengers": int
                }
              ]
            }

        """
        return super().list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        """
        Returns starship object information.

        ## 200 Response data

        Starship information

            {
                "id": int,
                "starship_class": string,
                "manufacturer": string,
                "length": float,
                "hyperdrive_rating": float,
                "cargo_capacity": int,
                "crew": int,
                "passengers": int
            }

        """
        return super().retrieve(request, *args, **kwargs)


class MarketFilter(filters.BaseFilterBackend):
    def get_schema_fields(self, view):
        return [
            coreapi.Field(
                name='starship_class',
                location='query',
                required=False,
                type='string',
                description='Starship class must contain',
                example='death star'
            ),
            coreapi.Field(
                name='sort',
                location='query',
                required=False,
                type='string',
                description=(
                    'Sort by. Possible values are: price (asc.), -price (desc.), created_at (asc.), -created_at (desc.)'
                )
            )
        ]


class MarketViewset(viewsets.generics.ListAPIView,
                    viewsets.generics.CreateAPIView,
                    viewsets.GenericViewSet):
    queryset = shiptrader_models.Listing.objects.all()
    serializer_class = shiptrader_serializers.ListingSerializer

    filter_backends = (MarketFilter, )

    def filter_queryset(self, queryset):
        return queryset.active_only()\
            .filter_by_starship_class(self.request.GET.get('starship_class'))\
            .sort(self.request.GET.get('sort'), available=('created_at', 'price'))

    def list(self, request, *args, **kwargs):
        """
        Find optimal starship.

        ## 200 Response

        Listing objects paginated response.

            {
              "count": int,
              "next": next page url,
              "previous": prev page url,
              "results": [
                {
                    "id": int,
                    "ship_type": int,
                    "name": string,
                    "price": int,
                    "is_active": bool,
                    "created_at": string date,
                    "updated_at": string date
                }
              ]
            }

        """
        return super().list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        """
        Create listing object for the starship.

        ## 201 Response

        Created successfully.

            {
                "id": int,
                "ship_type": int,
                "name": string,
                "price": int,
                "is_active": bool,
                "created_at": string date,
                "updated_at": string date
            }

        """
        return super().create(request, *args, **kwargs)


class ListingViewset(viewsets.generics.RetrieveAPIView,
                     viewsets.generics.UpdateAPIView,
                     viewsets.generics.DestroyAPIView,
                     viewsets.GenericViewSet):
    queryset = shiptrader_models.Listing.objects.all()
    serializer_class = shiptrader_serializers.ListingSerializer

    def retrieve(self, request, *args, **kwargs):
        """
        Returns listing object.

        ## 200 Response

        Listing information

            {
                "id": int,
                "ship_type": int,
                "name": string,
                "price": int,
                "is_active": bool,
                "created_at": string date,
                "updated_at": string date
            }

        """
        return super().retrieve(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        """
        Delete listing object.

        ## 204 Response

        Deleted successfully.

        """
        return super().destroy(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        """
        Update listing object.

        ## 204 Response

        Updated successfully.

            {
                "id": int,
                "ship_type": int,
                "name": string,
                "price": int,
                "is_active": bool,
                "created_at": string date,
                "updated_at": string date
            }

        """
        return super().update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        """
        Partial update listing object.

        ## 204 Response

        Updated successfully.

            {
                "id": int,
                "ship_type": int,
                "name": string,
                "price": int,
                "is_active": bool,
                "created_at": string date,
                "updated_at": string date
            }

        """
        return super().partial_update(request, *args, **kwargs)



