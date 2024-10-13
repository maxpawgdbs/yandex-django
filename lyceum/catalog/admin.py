from catalog import models

from django.contrib import admin


@admin.register(models.Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        models.Item.name.field.name,
        models.Item.is_published.field.name,
    )
    list_display_links = ("name",)
    list_editable = ("is_published",)
    list_display_links = ("id",)
    filter_horizontal = ("tags",)


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        models.Category.name.field.name,
        models.Category.is_published.field.name,
        models.Category.slug.field.name,
        models.Category.weight.field.name,
    )
    list_editable = (
        "name",
        "is_published",
        "slug",
        "weight",
    )
    list_display_links = ("id",)


@admin.register(models.Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        models.Tag.name.field.name,
        models.Tag.is_published.field.name,
        models.Tag.slug.field.name,
    )
    list_editable = (
        "name",
        "is_published",
        "slug",
    )
    list_display_links = ("id",)
