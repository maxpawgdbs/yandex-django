import django.db.transaction
from django.contrib import admin, messages

import catalog.models


@admin.register(catalog.models.Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = (
        catalog.models.Item.id.field.name,
        catalog.models.Item.name.field.name,
        catalog.models.Item.is_published.field.name,
    )
    list_display_links = (catalog.models.Item.name.field.name,)
    list_editable = (catalog.models.Item.is_published.field.name,)
    list_display_links = (catalog.models.Item.name.field.name,)
    filter_horizontal = (catalog.models.Item.tags.field.name,)


@admin.register(catalog.models.Category)
class CategoryAdmin(admin.ModelAdmin):
    def save_model(self, request, *args, **kwargs):
        with django.db.transaction.atomic():
            try:
                return super(CategoryAdmin, self).save_model(
                    request,
                    *args,
                    **kwargs,
                )
            except Exception as e:
                django.db.transaction.set_rollback(True)
                self.message_user(request, e, messages.ERROR)

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


@admin.register(catalog.models.Tag)
class TagAdmin(admin.ModelAdmin):
    def save_model(self, request, *args, **kwargs):
        with django.db.transaction.atomic():
            try:
                return super(TagAdmin, self).save_model(
                    request,
                    *args,
                    **kwargs,
                )
            except Exception as e:
                django.db.transaction.set_rollback(True)
                self.message_user(request, e, messages.ERROR)

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
