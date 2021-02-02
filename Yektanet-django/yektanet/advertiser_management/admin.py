from django.contrib import admin
from .models import Advertiser, Ad


class AdAdmin(admin.ModelAdmin):
    list_display = ('title', 'advertiser', 'approved')
    search_fields = ('title', 'advertiser')
    list_filter = ('approved',)


admin.site.register(Advertiser)
admin.site.register(Ad, AdAdmin)
