from rest_framework import serializers

from shiptrader import models as shiptrader_models


class StarshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = shiptrader_models.Starship
        fields = '__all__'


class ListingSerializer(serializers.ModelSerializer):
    ship_type = serializers.PrimaryKeyRelatedField(
        queryset=shiptrader_models.Starship.objects.all()
    )

    class Meta:
        model = shiptrader_models.Listing
        fields = '__all__'
