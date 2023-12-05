from django.contrib import admin
from Vet.models import Service, Doctor, Schedule
from django.utils.html import format_html
from django.forms import TextInput, Textarea
from django.db import models
from django import forms
# Register your models here.

admin.AdminSite.site_header = 'Администрирование Vetclinic'

class ServiceForm(forms.ModelForm):
    class Meta:
        widgets = {
            'image': TextInput(attrs={'size': '20'}),
        }

class ServiceAdmin(admin.ModelAdmin):
    list_display = ['service_name', 'price', 'description', 'image', 'show_image']
    list_display_links = ['service_name']
    list_editable = ['price', 'image']
    search_fields = ['service']
    form = ServiceForm

    def show_image(self, obj):
        return format_html('<image src="{}" style="height:200px" />', obj.image)
    show_image.short_description = 'Превью'

admin.site.register(Service, ServiceAdmin)


class ScheduleInline(admin.TabularInline):
    model = Schedule
    extra = 0

class DoctorAdmin(admin.ModelAdmin):
    list_display = ['doc_name', 'doc_spec']
    list_filter=['doc_spec']
    search_fields = ['doc_name', 'doc_spec']
    inlines = [ScheduleInline]
admin.site.register(Doctor, DoctorAdmin)


class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('display_doc_name', 'display_doc_spec', 'day', 'sch')
    list_filter = ['day']
    search_fields = ['doc__doc_name', 'doc__doc_spec']

admin.site.register(Schedule, ScheduleAdmin)


