from django.contrib import admin
from sitesetting.models import sitesetting,contact_us,privacy,rules
# Register your models here.

class filterxx(admin.ModelAdmin):
    list_display = ['__str__','subject']

    class meta:
        model=contact_us

admin.site.register(contact_us,filterxx)
admin.site.register(sitesetting)
admin.site.register(privacy)
admin.site.register(rules)
