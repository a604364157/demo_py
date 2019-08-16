from django.contrib import admin

from web.models import Student


class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'age')
    search_fields = ('name', 'age')


admin.site.register(Student, StudentAdmin)
