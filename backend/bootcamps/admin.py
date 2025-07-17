from django.contrib import admin
from django.utils.html import format_html
from .models import Bootcamp, Lead

@admin.register(Bootcamp)
class BootcampAdmin(admin.ModelAdmin):
    list_display = ('title', 'formatted_price', 'duration', 'next_session', 'description_short')
    list_filter = ('duration',)
    search_fields = ('title', 'description')
    ordering = ('next_session',)
    date_hierarchy = 'next_session'
    
    fieldsets = (
        (None, {
            'fields': ('title', 'description')
        }),
        ('Détails', {
            'fields': ('duration', 'price', 'next_session'),
            'classes': ('collapse',)
        }),
    )

    def formatted_price(self, obj):
        return f"{obj.price:,.0f} FCFA".replace(",", " ")
    formatted_price.short_description = 'Prix'
    formatted_price.admin_order_field = 'price'

    def description_short(self, obj):
        return f"{obj.description[:50]}..." if obj.description else ""
    description_short.short_description = "Description"

@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'formatted_phone', 'bootcamp_link', 'status', 'status_badge', 'created_at')
    list_editable = ('status',)  # On édite le champ réel plutôt que le badge
    list_filter = ('status', 'bootcamp', 'created_at')
    search_fields = ('name', 'email', 'phone', 'bootcamp__title')
    readonly_fields = ('created_at',)
    date_hierarchy = 'created_at'
    actions = ['mark_as_contacted']
    
    def formatted_phone(self, obj):
        if obj.phone:
            return f"{obj.phone[:3]} {obj.phone[3:5]} {obj.phone[5:8]} {obj.phone[8:]}"
        return ""
    formatted_phone.short_description = 'Téléphone'
    formatted_phone.admin_order_field = 'phone'

    def bootcamp_link(self, obj):
        if obj.bootcamp:
            return format_html(
                '<a href="/admin/bootcamps/bootcamp/{}/change/">{}</a>',
                obj.bootcamp.id,
                obj.bootcamp.title
            )
        return "-"
    bootcamp_link.short_description = 'Bootcamp'
    bootcamp_link.admin_order_field = 'bootcamp__title'

    def status_badge(self, obj):
        status_colors = {
            'NEW': '#ff7f2a',  # Orange Xarala
            'CONTACTED': '#db4061',  # Rose Xarala
            'REGISTERED': '#4CAF50'  # Vert
        }
        return format_html(
            '<span style="color: white; background-color: {}; padding: 3px 8px; border-radius: 10px; font-weight: bold;">{}</span>',
            status_colors.get(obj.status, '#607D8B'),
            obj.get_status_display()
        )
    status_badge.short_description = 'Statut Visuel'
    status_badge.admin_order_field = 'status'

    @admin.action(description="Marquer comme contacté")
    def mark_as_contacted(self, request, queryset):
        updated = queryset.update(status='CONTACTED')
        self.message_user(request, f"{updated} leads marqués comme contactés")