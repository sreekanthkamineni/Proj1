from django.contrib import admin

# Register your models here.
from .models import items, contact
class iteamAdmin(admin.ModelAdmin):
    list_display= ('name', 'price', 'is_breakfast', 'is_lunch', 'is_dinner','is_drinks')
    list_display_links = ('name',)
    list_editable = ('is_breakfast', 'is_lunch', 'is_dinner','is_drinks')
    list_filter = ('is_breakfast', 'is_lunch', 'is_dinner')
    search_fields = ('name','price')
    list_per_page = 25

admin.site.register(items,iteamAdmin)

class contactAdmin(admin.ModelAdmin):
    list_display = ('name','email','message')
    list_display_links = ('name',)
    list_per_page = 25


admin.site.register(contact,contactAdmin)