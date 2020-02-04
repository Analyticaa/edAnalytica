from django.contrib import admin
from org.models import Org

class OrgAdmin(admin.ModelAdmin):
    fields = ('org_id', 'name', 'description', 'logo', 'footer', 'users')

    class Meta:
        pass

admin.site.register(Org, OrgAdmin)
