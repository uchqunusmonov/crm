from django.contrib import admin

# Register your models here


from .models import Email

@admin.register(Email)
class EmailAdmin(admin.ModelAdmin):
    list_display = ('id', 'sender', 'subject', 'body', 'timestamp', 'read', 'archived')