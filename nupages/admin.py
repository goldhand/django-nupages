from django.contrib import admin

from .models import Page


class PageAdmin(admin.ModelAdmin):
	fields = ['title', 'description', 'content', 
	'status', 'activate_date', 'deactivate_date', 'custom_template', 'site']
	list_display = ['title', 'site', 'status',]
	list_filter = ['status', 'site']
	search_fields = ['title',]

admin.site.register(Page, PageAdmin)