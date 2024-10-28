import django.contrib
import django.forms
import tinymce.models

import catalog.models


class GaleryInline(django.contrib.admin.TabularInline):
    model = catalog.models.ItemGalery
    extra = 1


class MainImageInline(django.contrib.admin.TabularInline):
    model = catalog.models.MainImage
    extra = 1


class ItemAdminForm(django.forms.ModelForm):
    text = tinymce.models.HTMLField()

    class Meta:
        model = catalog.models.Item
        fields = ["text"]


@django.contrib.admin.register(catalog.models.Item)
class ItemAdmin(django.contrib.admin.ModelAdmin):
    form = ItemAdminForm
    list_display = (
        catalog.models.Item.id.field.name,
        catalog.models.Item.name.field.name,
        catalog.models.Item.is_published.field.name,
        catalog.models.Item.is_on_main.field.name,
        catalog.models.MainImage.image_tmb,
        catalog.models.Item.created_at.field.name,
        catalog.models.Item.updated_at.field.name
    )
    fields = (
        catalog.models.Item.name.field.name,
        catalog.models.Item.category.field.name,
        catalog.models.Item.tags.field.name,
        catalog.models.Item.text.field.name,
    )
    inlines = [MainImageInline, GaleryInline]
    list_display_links = (catalog.models.Item.name.field.name,)
    list_editable = (
        catalog.models.Item.is_published.field.name,
        catalog.models.Item.is_on_main.field.name,
    )
    filter_horizontal = (catalog.models.Item.tags.field.name,)


@django.contrib.admin.register(catalog.models.Category)
class CategoryAdmin(django.contrib.admin.ModelAdmin):
    list_display = (
        catalog.models.Category.id.field.name,
        catalog.models.Category.name.field.name,
        catalog.models.Category.is_published.field.name,
        catalog.models.Category.slug.field.name,
        catalog.models.Category.weight.field.name,
    )
    list_editable = (
        catalog.models.Category.name.field.name,
        catalog.models.Category.is_published.field.name,
        catalog.models.Category.slug.field.name,
        catalog.models.Category.weight.field.name,
    )
    list_display_links = (catalog.models.Category.id.field.name,)
    exclude = (catalog.models.Category.normalized_name.field.name,)


@django.contrib.admin.register(catalog.models.Tag)
class TagAdmin(django.contrib.admin.ModelAdmin):
    list_display = (
        catalog.models.Tag.id.field.name,
        catalog.models.Tag.name.field.name,
        catalog.models.Tag.is_published.field.name,
        catalog.models.Tag.slug.field.name,
    )
    list_editable = (
        catalog.models.Tag.name.field.name,
        catalog.models.Tag.is_published.field.name,
        catalog.models.Tag.slug.field.name,
    )
    list_display_links = (catalog.models.Tag.id.field.name,)
    exclude = (catalog.models.Tag.normalized_name.field.name,)


__all__ = (
    ItemAdmin,
    TagAdmin,
    CategoryAdmin,
)
