from django.urls import path

from . import views

urlpatterns = [
    path('', views.cursoscore, name='core'),
    path('cursos', views.cursos, name='cursos'),
    path('cursosing', views.cursosing, name='cursosing'),
    path('cursosdoc', views.cursosdoc, name='cursosdoc'),
    path('cursoshora', views.cursoshora, name='cursoshora'),
    path('cursosfecha', views.cursosfecha, name='cursosfecha'),
    path('cursosaula', views.cursosaula, name='cursosaula'),
    path('cursosreg', views.cursosreg, name='cursosreg'),
    path('postreg', views.postreg, name='postreg'),
]