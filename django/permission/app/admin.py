from django.contrib import admin
from .models import Test, Contact, Tag
# Register your models here.
class TagInline(admin.TabularInline):
    model = Tag
    extra = 0

class ContactAdmin(admin.ModelAdmin):
#    fields = ('name', 'email')
    search_fields = ('name',)
    list_display = ('name', 'age', 'email')
    inlines = [TagInline]
    fieldsets = (
                 ['main',{
                          'fields':('name', 'email'),
                    }],
                 ['advance',{
                             'classes':('collapse',),  #css格式：显示/隐藏
                             'fields':('age',),
                    }]
                 )
    
admin.site.register(Contact, ContactAdmin)
admin.site.register([Test])