from django import forms

from .models import Prompt


class PromptForm(forms.ModelForm):
    class Meta:
        model = Prompt
        fields = ["title", "use_case", "category", "prompt_text", "notes", "tags"]
        widgets = {
            "prompt_text": forms.Textarea(attrs={"rows": 8}),
            "notes": forms.Textarea(attrs={"rows": 3}),
        }
