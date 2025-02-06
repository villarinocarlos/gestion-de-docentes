from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('pantalla_principal')  # Redirige a pantalla principal después del login
        else:
            messages.error(request, "Usuario o contraseña incorrectos.")
    
    return render(request, "login.html")

@login_required
def pantalla_principal(request):
    return render(request, "pantalla_principal.html", {"role": request.user.role})


from django.contrib.auth.decorators import login_required

@login_required
def pantalla_principal(request):
    return render(request, "pantalla_principal.html", {"role": request.user.role})


from django.contrib.auth import logout

from django.contrib.auth import logout
from django.shortcuts import redirect

def logout_view(request):
    logout(request)  # Desconecta al usuario
    return redirect('login')  # Redirige a la página de login después de desconectar
