from django.contrib import admin

from .models import Category, Prompt


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(Prompt)
class PromptAdmin(admin.ModelAdmin):
    list_display = ("title", "use_case", "category", "updated_at")
    list_filter = ("use_case", "category")
    search_fields = ("title", "prompt_text", "tags")
