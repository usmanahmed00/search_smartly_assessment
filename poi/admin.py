from django.contrib import admin
from .models import PointOfInterest


class PointOfInterestAdmin(admin.ModelAdmin):
    list_display = ('internal_id', 'name', 'external_id', 'category', 'avg_rating')
    list_filter = ('category',)
    search_fields = ('internal_id', 'external_id')


admin.site.register(PointOfInterest, PointOfInterestAdmin)
