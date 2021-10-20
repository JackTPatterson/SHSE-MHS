from users.models import Announcement, Feedback, Dates, Inductees, Officers
from django.contrib import admin



# Register your models here.
admin.site.register(Feedback)

class AnnouncementAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)

class InducteesAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)

class OfficersAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)

admin.site.register(Announcement, AnnouncementAdmin)
admin.site.register(Dates)
admin.site.register(Inductees, InducteesAdmin)
admin.site.register(Officers, OfficersAdmin)




