from django.contrib import admin
from .models import Expend, Income, Member

# Register your models here.
@admin.register(Expend)
class ExpendAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'date', 'account', 'outcometype', 'people', 'money')
    ordering = ['id']

@admin.register(Income)
class IncomeAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'date', 'account', 'incometype', 'people', 'money')
    ordering = ['id']

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'member_name', 'member_relation')
    ordering = ['id']
