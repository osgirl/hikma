from django.contrib import admin

from .models import Product, State, City, Pharmacy, Doctor
# Register your models here.
#===============================================================================
'''
from django.contrib.admin.models import LogEntry, DELETION
from django.utils.html import escape
from django.core.urlresolvers import reverse

class LogEntryAdmin(admin.ModelAdmin):

    date_hierarchy = 'action_time'

    readonly_fields = LogEntry._meta.get_all_field_names()

    list_filter = [
        'user',
        'content_type',
        'action_flag'
    ]

    search_fields = [
        'object_repr',
        'change_message'
    ]


    list_display = [
        'action_time',
        'user',
        'content_type',
        'object_link',
        'action_flag',
        'change_message',
    ]

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return request.user.is_superuser and request.method != 'POST'

    def has_delete_permission(self, request, obj=None):
        return False

    def object_link(self, obj):
        if obj.action_flag == DELETION:
            link = escape(obj.object_repr)
        else:
            ct = obj.content_type
            link = u'<a href="%s">%s</a>' % (
                reverse('admin:%s_%s_change' % (ct.app_label, ct.model), args=[obj.object_id]),
                escape(obj.object_repr),
            )
        return link
    object_link.allow_tags = True
    object_link.admin_order_field = 'object_repr'
    object_link.short_description = u'object'
    
    def queryset(self, request):
        return super(LogEntryAdmin, self).queryset(request) \
            .prefetch_related('content_type')

admin.site.register(LogEntry, LogEntryAdmin)
'''
#===============================================================================
#class ChoiceInline(admin.TabularInline): #StackedInline
#    model = Choice
#    extra = 3

class ProductAdmin(admin.ModelAdmin):
    fieldsets = [
                 ("Product",            {'fields': ['product']}),
                 ("Image",            {'fields': ['image']}),
                 ("Product Image",      {'fields': ['image_thumb']}),
                 ]
#    inlines = [ChoiceInline]
    list_display = ['product', 'image_thumb']
    readonly_fields = ['image_thumb',]
    list_filter = ['product']
    search_fields = ['product']
    

admin.site.register(Product, ProductAdmin)
#===============================================================================
class StateAdmin(admin.ModelAdmin):
    fieldsets = [
                 ("State",            {'fields': ['state']}),
                 ]
#    inlines = [ChoiceInline]
    list_display = ['state']
    list_filter = ['state']
    search_fields = ['state']
    

admin.site.register(State, StateAdmin)
#===============================================================================
class CityAdmin(admin.ModelAdmin):
    fieldsets = [
                 ("City",   {'fields': ['city']}),
                 ("State",  {'fields': ['state']}),
                 ]
#    inlines = [ChoiceInline]
    list_display = ['city', 'state']
    list_filter = ['city', 'state']
    search_fields = ['city', 'state__state']
    

admin.site.register(City, CityAdmin)
#===============================================================================
class PharmacyAdmin(admin.ModelAdmin):
    fieldsets = [
                 ("Pharmacy",   {'fields': ['pharmacy']}),
                 ("city",       {'fields': ['city']}),
                 ]
#    inlines = [ChoiceInline]
    list_display = ['pharmacy', 'city']
    list_filter = ['pharmacy', 'city']
    search_fields = ['pharmacy', 'city__city']
    

admin.site.register(Pharmacy, PharmacyAdmin)
#===============================================================================