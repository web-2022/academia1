# apps/courses/views.py

from django.shortcuts import render, get_object_or_404, redirect
from .models import Course, Chapter, Purchase, Inicio, CiclosAcademia
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

def course_list(request):
    courses = Course.objects.all()
    return render(request, 'courses/course_list.html', {'courses': courses})

def course_detail(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    chapters = Chapter.objects.filter(course=course).order_by('order')
    
    # Verificar si el usuario está autenticado y ha comprado el curso
    has_purchased = False
    if request.user.is_authenticated:
        has_purchased = Purchase.objects.filter(user=request.user, course=course).exists()

    # Si el usuario ha comprado el curso, mostrar todos los capítulos
    if has_purchased:
        free_chapters = chapters  # Todos los capítulos son accesibles
        locked_chapters = []
    else:
        free_chapters = chapters[:2]  # Los primeros dos capítulos son gratuitos
        locked_chapters = chapters[2:]  # Los demás capítulos están bloqueados

    context = {
        'course': course,
        'free_chapters': free_chapters,
        'locked_chapters': locked_chapters,
        'has_purchased': has_purchased
    }

    return render(request, 'courses/course_detail.html', context)

@login_required
def full_course_detail(request, course_id):
    course = get_object_or_404(Course, id=course_id)

    # Verificar si el usuario ha comprado el curso
    has_purchased = Purchase.objects.filter(user=request.user, course=course).exists()

    if not has_purchased:
        return redirect('purchase_course', course_id=course_id)

    chapters = Chapter.objects.filter(course=course).order_by('order')
    return render(request, 'courses/full_course_detail.html', {'course': course, 'chapters': chapters})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Después de registrarse, lo redirigimos al login
    else:
        form = UserCreationForm()

    return render(request, 'registration/register.html', {'form': form})

#Bienvenida al usuario
def bienvenida (request):
    context = {
        'user': request.user # Aquí pasando el usuario al contexto
    }
    return render(request,'courses/course_detail.html',context)

#Bienvenida al usuario
def inicio (request): 
    inicios = Inicio.objects.all() # obtenemos todos los datos de inicio   
    return render(request,'courses/inicio.html', {'inicios': inicios})

def ciclos (request):  
    ciclos = CiclosAcademia.objects.all() # obtenemos todos los datos de la tabla CiclosAcademia
    return render(request,'courses/ciclos.html', {'ciclos': ciclos})


def contactanos (request):     
    return render(request,'courses/contactanos.html')

