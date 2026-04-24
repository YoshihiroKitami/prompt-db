from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render

from .forms import PromptForm
from .models import Prompt


def prompt_list(request):
    query = request.GET.get("q", "").strip()
    prompts = Prompt.objects.select_related("category")

    if query:
        prompts = prompts.filter(
            Q(title__icontains=query)
            | Q(use_case__icontains=query)
            | Q(tags__icontains=query)
            | Q(prompt_text__icontains=query)
        )

    return render(request, "prompts/prompt_list.html", {"prompts": prompts, "query": query})


def prompt_create(request):
    if request.method == "POST":
        form = PromptForm(request.POST)
        if form.is_valid():
            prompt = form.save()
            return redirect("prompt-detail", pk=prompt.pk)
    else:
        form = PromptForm()

    return render(request, "prompts/prompt_form.html", {"form": form})


def prompt_detail(request, pk):
    prompt = get_object_or_404(Prompt.objects.select_related("category"), pk=pk)
    return render(request, "prompts/prompt_detail.html", {"prompt": prompt})
