from django.shortcuts import render, redirect
from .models import CursosV2, DocentesV2, Horas, Fechas, Aulas, IngenieriaV2, Registros


def index(request):
    	return render(request, 'core.html', {})

def cursos(request, *args, **kargs):
		cursos=CursosV2.objects.all()
		buscar = request.POST['buscalo']
		cursos = cursos.filter(IdCurso__contains= buscar)
		NameDocentes = DocentesV2.objects.all()
		HorasList=Horas.objects.all()
		FechasList= Fechas.objects.all()
		AulasList=Aulas.objects.all()
		IngenieriaList = IngenieriaV2.objects.all()
		return render(request, "cursos.html",{"cursos":cursos,"NameDocentes":NameDocentes,
	    	"HorasList":HorasList, "FechasList":FechasList, "AulasList":AulasList,"IngenieriaList":IngenieriaList})

def cursosing(request, *args, **kargs):
		cursos=CursosV2.objects.all()
		buscar = request.POST['buscalo']
		print(buscar)
		cursos = cursos.filter(Ingenieria= buscar)
		NameDocentes = DocentesV2.objects.all()
		HorasList=Horas.objects.all()
		FechasList= Fechas.objects.all()
		AulasList=Aulas.objects.all()
		IngenieriaList = IngenieriaV2.objects.all()
		return render(request, "cursos.html",{"cursos":cursos,"NameDocentes":NameDocentes,
	    	"HorasList":HorasList, "FechasList":FechasList, "AulasList":AulasList,"IngenieriaList":IngenieriaList})

def cursosaula(request, *args, **kargs):
		cursos=CursosV2.objects.all()
		buscar = request.POST['buscalo']
		cursos = cursos.filter(Aula= buscar)
		NameDocentes = DocentesV2.objects.all()
		HorasList=Horas.objects.all()
		FechasList= Fechas.objects.all()
		AulasList=Aulas.objects.all()
		IngenieriaList = IngenieriaV2.objects.all()
		return render(request, "cursos.html",{"cursos":cursos,"NameDocentes":NameDocentes,
	    	"HorasList":HorasList, "FechasList":FechasList, "AulasList":AulasList,"IngenieriaList":IngenieriaList})

def cursosfecha(request, *args, **kargs):
		cursos=CursosV2.objects.all()
		buscar = request.POST['buscalo']
		cursos = cursos.filter(Fecha= buscar)
		NameDocentes = DocentesV2.objects.all()
		HorasList=Horas.objects.all()
		FechasList= Fechas.objects.all()
		AulasList=Aulas.objects.all()
		IngenieriaList = IngenieriaV2.objects.all()
		return render(request, "cursos.html",{"cursos":cursos,"NameDocentes":NameDocentes,
	    	"HorasList":HorasList, "FechasList":FechasList, "AulasList":AulasList,"IngenieriaList":IngenieriaList})

def cursoshora(request, *args, **kargs):
		cursos=CursosV2.objects.all()
		buscar = request.POST['buscalo']
		cursos = cursos.filter(Hora= buscar)
		NameDocentes = DocentesV2.objects.all()
		HorasList=Horas.objects.all()
		FechasList= Fechas.objects.all()
		AulasList=Aulas.objects.all()
		IngenieriaList = IngenieriaV2.objects.all()
		return render(request, "cursos.html",{"cursos":cursos,"NameDocentes":NameDocentes,
	    	"HorasList":HorasList, "FechasList":FechasList, "AulasList":AulasList,"IngenieriaList":IngenieriaList})

def cursosdoc(request, *args, **kargs):
		cursos=CursosV2.objects.all()
		buscar = request.POST['buscalo']
		cursos = cursos.filter(id= buscar)
		NameDocentes = DocentesV2.objects.all()
		HorasList=Horas.objects.all()
		FechasList= Fechas.objects.all()
		AulasList=Aulas.objects.all()
		IngenieriaList = IngenieriaV2.objects.all()
		return render(request, "cursos.html",{"cursos":cursos,"NameDocentes":NameDocentes,
	    	"HorasList":HorasList, "FechasList":FechasList, "AulasList":AulasList,"IngenieriaList":IngenieriaList})


def cursosreg(request, *args, **kargs):
		cursos = CursosV2.objects.all()
		buscar = request.POST['buscalo']
		print(buscar)
		cursos = cursos.filter(id= buscar)
		NameDocentes = DocentesV2.objects.all()
		HorasList = Horas.objects.all()
		FechasList = Fechas.objects.all()
		AulasList = Aulas.objects.all()
		IngenieriaList = IngenieriaV2.objects.all()
		return render(request, "register.html",{"cursosreg":cursos,"NameDocentes":NameDocentes,
	    	"HorasList":HorasList, "FechasList":FechasList, "AulasList":AulasList,"IngenieriaList":IngenieriaList})

def cursoscore(request):
	    cursoscore=CursosV2.objects.all()
	    NameDocentes = DocentesV2.objects.all()
	    HorasList = Horas.objects.all()
	    FechasList = Fechas.objects.all()
	    AulasList = Aulas.objects.all()
	    IngenieriaList = IngenieriaV2.objects.all()
	    return render(request, "core.html",{"cursoscore":cursoscore,"NameDocentes":NameDocentes,
	    	"HorasList":HorasList, "FechasList":FechasList, "AulasList":AulasList,"IngenieriaList":IngenieriaList})


def postreg(request, *args, **kargs):
	curso= CursosV2.objects.all()
	name = request.POST['name']
	lastnameP = request.POST['lastnameP']
	lastnameM = request.POST['lastnameM']
	email = request.POST['email']
	idC = request.POST['buscalo']
	curso = curso.filter(id = idC)
	for t in curso:
		print(t.Fecha)
		x = str(t.Fecha).split("/")
		fecha = x[2] + '-' + x[1] + '-' + x[0]
		fecha = str(fecha)
		print(fecha)

		p =Registros(Nombre = name, ApellidoP = lastnameP,ApellidoM = lastnameM,
			Email = email, Curso = t.Curso, Docente = t.Docente, Hora = str(t.Hora),
			Fecha = str(fecha), Aula = t.Aula, Ingenieria = t.Ingenieria)
	p.save()
	return redirect('/')