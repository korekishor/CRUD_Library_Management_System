from django.contrib import admin
from .models import data, Record
from .models import hirebook


# Register your models here.
@admin.register(data)
class dataadmin(admin.ModelAdmin):
    list_display = ('id','book_name','author_name','price')

@admin.register(Record)
class recordadmin(admin.ModelAdmin):
    list_display = ['id','ename','email','mobile','password','dob']

@admin.register(hirebook)
class hirebookAdmin(admin.ModelAdmin):
    list_display = ['id','student_name','book_name','book_id','hire_date','issu_date','due','due2']

