from django.contrib import admin

from map.models import Well

admin.site.register(Well)

admin.site.site_header = "إدارة الآبار"

admin.site.site_title = "إدارة الآبار"
admin.site.index_title = "إدارة الآبار"
