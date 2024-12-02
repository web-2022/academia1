# apps/courses/views.py

from django.shortcuts import render, get_object_or_404, redirect
from .models import Course, Chapter, Purchase, Inicio, CiclosAcademia
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

def course_list(request):
    courses = Course.objects.all()
    return render(request, 'courses/global/course_list.html', {'courses': courses})

def course_detail(request, slug):
    course = get_object_or_404(Course, slug=slug)
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

    return render(request, 'courses/global/course_detail.html', context)

@login_required
def full_course_detail(request, slug):
    course = get_object_or_404(Course, slug=slug)

    # Verificar si el usuario ha comprado el curso
    has_purchased = Purchase.objects.filter(user=request.user, course=course).exists()

    if not has_purchased:
        return redirect('purchase_course', slug=slug)

    chapters = Chapter.objects.filter(course=course).order_by('order')
    return render(request, 'courses/global/full_course_detail.html', {'course': course, 'chapters': chapters})

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
    return render(request,'courses/global/course_detail.html',context)

#Bienvenida al usuario
def inicio (request): 
    inicios = Inicio.objects.all() # obtenemos todos los datos de inicio   
    return render(request,'courses/global/inicio.html', {'inicios': inicios})

def ciclos (request):  
    ciclos = CiclosAcademia.objects.all() # obtenemos todos los datos de la tabla CiclosAcademia
    return render(request,'courses/global/ciclos.html', {'ciclos': ciclos})


def contactanos (request):     
    return render(request,'courses/global/contactanos.html')

# Generando vistas dinámicas
def capitulo(request, course_slug, chapter_slug):
    # Obtener el curso utilizando su slug
    course = get_object_or_404(Course, slug=course_slug)

    # Obtener el capítulo utilizando su slug y asegurándonos de que pertenece al curso correcto
    chapter = get_object_or_404(Chapter, slug=chapter_slug, course=course)

    # Contexto para pasar el capítulo y el curso a la plantilla
    context = {
        'course': course,
        'chapter': chapter,
    }

    # Si deseas generar dinámicamente el nombre de la plantilla en función del capítulo
    # Esto solo es útil si cada capítulo tiene su propia plantilla, por ejemplo: capitulo_1.html
    template_name = f'courses/3años/{chapter_slug}.html'

    try:
        # Renderiza la plantilla del capítulo
        return render(request, template_name, context)
    except Exception as e:
        # Si la plantilla no se encuentra, maneja el error (puedes usar una página de error)
        return render(request, 'courses/global/404.html', {'error': str(e)})