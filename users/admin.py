from users.models import Announcement, Feedback
from django.contrib import admin

# Register your models here.
admin.site.register(Feedback)

class AnnouncementAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)

admin.site.register(Announcement, AnnouncementAdmin)
