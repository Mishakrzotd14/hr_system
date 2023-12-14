from django.contrib import admin
from .models import Employee


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'position', 'manager', 'salary', 'salary_info')
    list_filter = ('position', 'hierarchy_level')
    actions = ['delete_salary_info']

    @admin.action(description='Delete all information about the paid salary')
    def delete_salary_info(self, request, queryset):
        queryset.update(salary_info='')


admin.site.register(Employee, EmployeeAdmin)



