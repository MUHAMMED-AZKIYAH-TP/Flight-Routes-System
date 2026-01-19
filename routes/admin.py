from django.contrib import admin
from .models import Airport, AirportRoute


@admin.register(Airport)
class AirportAdmin(admin.ModelAdmin):
    list_display = ("code",)
    search_fields = ("code",)


@admin.register(AirportRoute)
class AirportRouteAdmin(admin.ModelAdmin):
    list_display = (
        "airport",
        "left",
        "right",
        "distance_km",
        "duration_min",
    )
    list_filter = ("duration_min",)
    search_fields = ("airport__code",)
