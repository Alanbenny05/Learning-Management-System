from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from courses.models import Note

# Create your views here.
def home(request):
    return render(request, 'core/home.html')

@login_required
def dashboard(request):
    try: 
        profile = request.user.profile
    except:
        return redirect('accounts:login')
    
    notes = Note.objects.all()  # All notes visible to all users
    user_notes = Note.objects.filter(uploaded_by=request.user)  # Notes uploaded by current user

    if profile.role == 'teacher':
        return render(request, 'core/teacher_dashboard.html', {'notes': notes, 'user_notes': user_notes})
    else:
        return render(request, 'core/student_dashboard.html', {'notes': notes})