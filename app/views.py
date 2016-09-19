from app.models import EspecieDocumental
from app.models import Setor
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.models import User


@csrf_protect
def cadastroUsuario(request):
    if request.POST:
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        email = request.POST.get('email', None)
        nome = request.POST.get('firstname', None)
        sobrenome = request.POST.get('lastname', None)
        user = User.objects.create_user(username, email, password)
        user.first_name = nome
        user.last_name = sobrenome
        user.save()
        if user.is_active:
            return HttpResponseRedirect(request.POST.get('next'))

    return render(request, 'cadastroUsuario.html')


@csrf_protect
@login_required
def home(request):
    return render(request, 'home.html')

@csrf_protect
@login_required
def user_detail(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.POST:
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        email = request.POST.get('email', None)
        nome = request.POST.get('firstname', None)
        sobrenome = request.POST.get('lastname', None)
        user = User.objects.get(id=pk)
        user.username = username
        user.email = email
        if user.password != password:
            user.password = make_password(password)
        user.first_name = nome
        user.last_name = sobrenome
        user.save()
        messages.success(request, 'Os dados foram atualizados com sucesso.')
    return render(request, 'editarUsuario.html', {'user': user})

@csrf_protect
@login_required
def especieDocumental(request):
    if request.POST:
        nome = request.POST.get('nome', None)
        EspecieDocumental.objects.create(nome=nome)
        return HttpResponseRedirect(request.POST.get('next'))
    return render(request, 'especieDocumental.html', {})

@csrf_protect
@login_required
def especiesDocumentais_list(request):
    especiesDocumentais = EspecieDocumental.objects.all
    return render(request, 'especiesDocumentais_list.html', {'especiesDocumentais': especiesDocumentais})

@csrf_protect
@login_required
def especieDocumental_remove(request, pk):
    especieDocumental = get_object_or_404(EspecieDocumental, pk=pk)
    especieDocumental.delete()
    return redirect('app.views.especiesDocumentais_list')

@csrf_protect
@login_required
def especieDocumental_edit(request, pk):
    especieDocumental = get_object_or_404(EspecieDocumental, pk=pk)
    if request.POST:
        nome = request.POST.get('nome', None)
        especieDocumental.nome = nome
        especieDocumental.save()
        return HttpResponseRedirect(request.POST.get('next'))
    return render(request, 'editarEspecieDocumental.html', {'especieDocumental': especieDocumental})

@csrf_protect
@login_required
def setor(request):
    if request.POST:
        nome = request.POST.get('nome',None)
        sigla = request.POST.get('sigla',None)
        funcao = request.POST.get('funcao',None)
        setor = Setor.objects.create(nome=nome, sigla=sigla, funcao=funcao)
        setor.save()
        return HttpResponseRedirect(request.POST.get('next'))
    return render(request, 'cadastro_setor.html', {})

@csrf_protect
@login_required
def setores_list(request):
    setores = Setor.objects.all
    return render(request, 'setores_list.html', {'setores': setores})

@csrf_protect
@login_required
def setor_edit(request, pk):
    setor = get_object_or_404(Setor, pk=pk)
    if request.POST:
        nome = request.POST.get('nome', None)
        sigla = request.POST.get('sigla', None)
        funcao = request.POST.get('funcao', None)
        setor.nome = nome
        setor.sigla=sigla
        setor.funcao=funcao
        setor.save()
        return HttpResponseRedirect(request.POST.get('next'))
    return render(request, 'editarSetor.html', {'setor': setor})

@csrf_protect
@login_required
def setor_remove(request, pk):
    setor = get_object_or_404(Setor, pk=pk)
    setor.delete()
    return redirect('app.views.setores_list')


