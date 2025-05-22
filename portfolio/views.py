from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .form import RegistrationForm
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib import messages
from .decorators import in_editor_group, group_required
from django.contrib.auth.decorators import user_passes_test




# Home page is accessible to everyone
def home(request):
    return render(request, 'portfolio/index.html')

# Registration view
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You can now log in.')
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'portfolio/register.html', {'form': form})

# All other pages require login
@login_required
def stage_1(request):
    return render(request, 'portfolio/stage_1.html')
    
@login_required
def stage_2(request):
    return render(request, 'portfolio/stage_2.html')
    
@login_required
def stage_3(request):
    return render(request, 'portfolio/stage_3.html')
    

def portfolio_page(request):
    return render(request, 'portfolio/portfolio_page.html')

# Add this function to your views.py


def logout_view(request):
    logout(request)
    messages.success(request, "You have been successfully logged out.")
    return redirect('home')

# Add to portfolio/views.py
from django.shortcuts import redirect

def switch_language(request):
    """
    Switch the language based on the POST request and redirect back.
    """
    if request.method == 'POST':
        language = request.POST.get('language', 'en')
        request.session['language'] = language
        
        # Get the next URL or default to home
        next_url = request.POST.get('next', '/')
        
    return redirect(next_url)
