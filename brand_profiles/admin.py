from django.contrib import admin
from brand_profiles.models import Category, Page, Brand_Identities, Reviews, Tours, Promotions

# Register your models here.
admin.site.register(Category)
admin.site.register(Page)
admin.site.register(Brand_Identities)
admin.site.register(Reviews)
admin.site.register(Tours)
admin.site.register(Promotions)
