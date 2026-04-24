from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ["name"]

    def __str__(self) -> str:
        return self.name


class Prompt(models.Model):
    title = models.CharField("タイトル", max_length=150)
    use_case = models.CharField("用途", max_length=100, help_text="例: 画像生成, LP作成, SNS投稿")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    prompt_text = models.TextField("プロンプト本文")
    notes = models.TextField("メモ", blank=True)
    tags = models.CharField("タグ", max_length=255, blank=True, help_text="カンマ区切りで入力")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-updated_at"]

    def __str__(self) -> str:
        return self.title
