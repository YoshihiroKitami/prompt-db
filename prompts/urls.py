from django.urls import path

from . import views

urlpatterns = [
    path("", views.prompt_list, name="prompt-list"),
    path("prompts/new/", views.prompt_create, name="prompt-create"),
    path("prompts/<int:pk>/", views.prompt_detail, name="prompt-detail"),
]
