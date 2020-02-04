from django.contrib import admin
from org.models import Org

class OrgAdmin(admin.ModelAdmin):
    fields = ('org_id', 'name', 'description', 'logo', 'footer', 'users')

    class Meta:
        pass

    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        obj.modified_by = request.user
        super().save_model(request, obj, form, change)


admin.site.register(Org, OrgAdmin)
