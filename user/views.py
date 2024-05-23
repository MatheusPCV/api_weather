from django.shortcuts import redirect, render
from django.views import View
from django.http import HttpRequest, HttpResponse, JsonResponse
from .authentication import *
from .models import UserEntity
from .forms import UserForm
from .repositories import UserRepository
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render, get_object_or_404



class UserTokenizer(View):
    def get(self, request):
        user = authenticate(username='user', password='a1b2c3')
        if user:
            return HttpResponse(generateToken(user))
        return HttpResponse('Username and/or password incorret')

class UserRegister(View):
    def get(self, request):
        form = UserForm()
        return render(request, 'user_register.html', {'form': form})

    def post(self, request):
        form = UserForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            repository = UserRepository(collectionName='users')
            repository.insert(data)
            return redirect('Weather View')
        else:
            return JsonResponse({"error": form.errors}, status=400)
        
class UserLogin(View):
    def get(self, request):
        return render(request, 'user_login.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            # Autenticação bem-sucedida
            login(request, user)
            return redirect('Weather View')
        else:
            # Autenticação falhou
            return render(request, 'user_login.html', {'error': 'Invalid username or password'})

def edit_user_view(request, user_id):
    # Obtém o usuário para edição
    user = get_object_or_404(User, id=user_id)

    if request.method == 'POST':
        # Se o formulário for enviado
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'User updated successfully.')
            return redirect('user_detail', user_id=user_id)
    else:
        # Se for uma solicitação GET, preencha o formulário com os dados do usuário
        form = UserForm(instance=user)

    return render(request, 'edit_user.html', {'form': form})