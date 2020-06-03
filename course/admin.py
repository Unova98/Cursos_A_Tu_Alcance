from django.contrib import admin
from .models import Cursos, Docentes, CursosV2, DocentesV2, IngenieriaV2, Horas, Aulas, Fechas, CursosList, Registros, Images

admin.site.register(CursosV2)
admin.site.register(DocentesV2)
admin.site.register(IngenieriaV2)
admin.site.register(CursosList)
admin.site.register(Horas)
admin.site.register(Fechas)
admin.site.register(Aulas)
admin.site.register(Registros)
admin.site.register(Images)