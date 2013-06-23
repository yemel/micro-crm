from django.contrib import admin
from core import models
from django import forms
from django.db.models import Q


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


class SimpleJobInline(admin.TabularInline):
    model = models.SimpleJob
    extra = 0
    fields = ('service', 'status', 'price')
    readonly_fields = ('price', 'status', 'service')

    def has_add_permission(self, request):
        return False


class RegularJobInline(admin.TabularInline):
    model = models.RegularJob
    extra = 0
    fields = ('service', 'status', 'price')
    readonly_fields = ('price', 'status', 'service')

    def has_add_permission(self, request):
        return False


class ClientAdmin(admin.ModelAdmin):
    list_display = ('company', 'contact', 'category', 'cuit')
    list_filter = ('category',)
    search_fields = ('company', 'contact', 'cuit')
    inlines = [SimpleJobInline, RegularJobInline]


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'kind')
    list_filter = ('category', 'kind')
    search_fields = ('name',)


class ServiceTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)


class SimpleJobForm(forms.ModelForm):
    service = forms.ModelChoiceField(queryset=models.Service.objects.filter(kind='simple').order_by('category'))

    class Meta:
        model = models.SimpleJob


class SimpleJobAdmin(admin.ModelAdmin):
    list_display = ('client', 'service', 'price', 'status', 'created')
    list_filter = ('status', 'service', 'created')
    search_fields = ('client__company', 'client__contact', 'client__cuit')
    fields = ('status', 'client', 'service', 'price', 'advance', 'deadline', 'comments')
    form = SimpleJobForm


class RegularJobForm(forms.ModelForm):
    service = forms.ModelChoiceField(queryset=models.Service.objects.filter(Q(kind='month') or Q(kind='anual')).order_by('category'))

    class Meta:
        model = models.SimpleJob


class RegularJobAdmin(admin.ModelAdmin):
    list_display = ('client', 'service', 'price', 'status', 'created')
    list_filter = ('status', 'service', 'created')
    search_fields = ('client__company', 'client__contact', 'client__cuit')
    fields = ('status', 'client', 'service', 'price', 'start_date', 'end_date', 'comments')
    form = RegularJobForm

admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.Client, ClientAdmin)
admin.site.register(models.Service, ServiceAdmin)
admin.site.register(models.ServiceType, ServiceTypeAdmin)
admin.site.register(models.SimpleJob, SimpleJobAdmin)
admin.site.register(models.RegularJob, RegularJobAdmin)
