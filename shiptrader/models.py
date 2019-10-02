from django.db import models


class Starship(models.Model):
    starship_class = models.CharField(max_length=255)
    manufacturer = models.CharField(max_length=255)

    length = models.FloatField()
    hyperdrive_rating = models.FloatField()
    cargo_capacity = models.BigIntegerField()

    crew = models.IntegerField()
    passengers = models.IntegerField()

    def __str__(self):
        return '{self.manufacturer} {self.starship_class}'.format(self=self)


class ListingManager(models.QuerySet):
    def active_only(self):
        return self.filter(is_active=True)

    def inactive_only(self):
        return self.filter(is_active=False)

    def filter_by_starship_class(self, ship_class):
        ship_class = str(ship_class or '').strip()
        if not ship_class:
            return self

        return self.filter(ship_type__starship_class__icontains=ship_class)

    def sort(self, value, available=None):
        value = list(filter(lambda x: len(x), str(value or '').strip().split(',')))
        if not value:
            return self

        if available:
            value = filter(lambda x: x.strip('-') in available, value)

        return self.order_by(*list(value))


class Listing(models.Model):
    objects = ListingManager.as_manager()

    name = models.CharField(max_length=255)
    ship_type = models.ForeignKey(Starship, related_name='listings', on_delete=models.CASCADE)
    price = models.BigIntegerField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    is_active = models.BooleanField(default=True, null=False, blank=True)

    def __str__(self):
        return '{self.name} {self.ship_type} ({self.price:,} CR)'.format(self=self)
