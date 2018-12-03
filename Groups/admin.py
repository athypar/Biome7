from django.contrib import admin
from . import models

# Register your models here.

class GroupMemberInline(admin.TabularInline):
    model = models.GroupMember

class UserAccountsAdmin(admin.ModelAdmin):
    pass

admin.site.register(models.Group,UserAccountsAdmin)
