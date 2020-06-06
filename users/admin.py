from django.contrib import admin
from users.models import UserProfile


# Register your models here.
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'card')


admin.site.register(UserProfile, UserProfileAdmin)
admin.site.site_header = '不动产查询管理系统'
admin.site.site_title = '不动产查询'
