from django.contrib import admin

import catalog.models


@admin.register(catalog.models.Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "is_published",
    )
    list_display_links = ("name",)
    list_editable = ("is_published",)
    list_display_links = ("name",)
    filter_horizontal = ("tags",)


@admin.register(catalog.models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "is_published",
        "slug",
        "weight",
    )
    list_editable = (
        "name",
        "is_published",
        "slug",
        "weight",
    )
    list_display_links = ("id",)


@admin.register(catalog.models.Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "is_published",
        "slug",
    )
    list_editable = (
        "name",
        "is_published",
        "slug",
    )
    list_display_links = ("id",)
