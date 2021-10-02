from django.contrib import admin

# Register your models here.
from django.contrib.admin import ModelAdmin

from pypro.turmas.models import Turma, Matricula


class MatriculaInline(admin.TabularInline):
    model = Matricula
    extra = 0
    ordering = ('-data',)
    autocomplete_fields = ('usuario',)
    readonly_fields = ('data',)

    def has_change_permission(self, request, obj=None):
        return False


@admin.register(Turma)
class TurmaAdmin(ModelAdmin):
    inlines = [
        MatriculaInline,
    ]
    list_display = ('nome', 'slug', 'inicio', 'fim')
    prepopulated_fields = {'slug': ('nome',)}
    ordering = ('-inicio',)
