from django.contrib import admin
from .models import Tarefa

admin.site.register(Tarefa)
class TarefaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'prazo', 'status')





# Register your models here.
