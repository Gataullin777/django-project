from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet
from .models import Article, Relation, Theme

class RelationInlineFormSet(BaseInlineFormSet):
    def clean(self):
        True_list = []
        for form in self.forms:
            form.cleaned_data
            boolean_checkbox_is_main = form.cleaned_data['is_main']

            status_checkbox_delete_article = form.cleaned_data["DELETE"]

            if boolean_checkbox_is_main is True and status_checkbox_delete_article is True:
                raise ValidationError('Нельзя удалять выбранную основную тему')

            if boolean_checkbox_is_main is True:
                True_list.append(boolean_checkbox_is_main)

        if len(True_list) > 1:
            raise ValidationError('Можно выбрать только одну тему')

        elif len(True_list) <= 0:
            raise ValidationError('Выберите основную тему')

        elif len(True_list) == 1:
            True_list.clear()
            return super().clean()




class RelationInline(admin.TabularInline):
    model = Relation
    extra = 0
    formset = RelationInlineFormSet

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):

    inlines = [RelationInline]

@admin.register(Theme)
class ThemeAdmin(admin.ModelAdmin):
    pass
