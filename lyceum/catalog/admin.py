import catalog.models

from django.contrib import admin


@admin.register(catalog.models.Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        catalog.models.Item.name.field.name,
        catalog.models.Item.is_published.field.name,
    )
    list_display_links = ("name",)
    list_editable = ("is_published",)
    list_display_links = ("id",)
    filter_horizontal = ("tags",)


@admin.register(catalog.models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        catalog.models.Category.name.field.name,
        catalog.models.Category.is_published.field.name,
        catalog.models.Category.slug.field.name,
        catalog.models.Category.weight.field.name,
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
        catalog.models.Tag.name.field.name,
        catalog.models.Tag.is_published.field.name,
        catalog.models.Tag.slug.field.name,
    )
    list_editable = (
        "name",
        "is_published",
        "slug",
    )
    list_display_links = ("id",)
