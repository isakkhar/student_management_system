from django.contrib import admin
admin.site.site_header = "M.R.M High School"
admin.site.site_title = "M.R.M High School"
admin.site.index_title = "M.R.M High School"
# Register your models here.
from django.contrib.auth.admin import UserAdmin

from student_management_app.models import CustomUser


class UserModel(UserAdmin):
    pass

admin.site.register(CustomUser,UserModel)
