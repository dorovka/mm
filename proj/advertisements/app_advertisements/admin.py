from django.contrib import admin
from .models import Advertisement

class Advertisementadmin(admin.ModelAdmin):
    list_display = ['title', 'descriptions', 'price', 'trades',  'date_update']
    list_filter = ['date_now', 'date_update', 'trades']
    fieldsets= (('Первый блок', {'fields' : ('title', 'descriptions')}),
    ('Второй блок', {'classes' : ('collapse',), 'fields' : ('price', 'trades')}),
    )
    actions = ['make_true', 'make_false', 'created_date']
    
    @admin.action(description='Обновить торг на True')
    def make_true(self, request, queryset):
        queryset.update(trades = True)
        pass

    @admin.action(description='Обновить торг на False')
    def make_false(self, request, queryset):
        queryset.update(trades = False)
        pass

admin.site.register(Advertisement, Advertisementadmin)
# Register your models here.
