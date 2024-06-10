from django.shortcuts import render, redirect
from .models import Pessoa

def home(request):
    pessoas = Pessoa.objects.all()
    return render(request,"index.html", {"pessoas":pessoas})

def salvar(request):
    vnome=request.POST.get("nome")
    vcidade=request.POST.get("cidade")
    vtipo=request.POST.get("tipo")
    Pessoa.objects.create(nome=vnome, cidade=vcidade, tipo=vtipo)
    pessoas = Pessoa.objects.all()
    return render(request, "index.html", {"pessoas":pessoas})

def editar(request, id):
    pessoa = Pessoa.objects.get(id=id)
    return render(request, "update.html", {"pessoa": pessoa})

def update(request, id):
    vnome=request.POST.get("nome")
    vcidade=request.POST.get("cidade")
    vtipo=request.POST.get("tipo")
    pessoa = Pessoa.objects.get(id=id)
    pessoa.nome = vnome
    pessoa.cidade = vcidade
    pessoa.tipo = vtipo
    pessoa.save()
    return redirect(home)

def delete(request, id):
    pessoa = Pessoa.objects.get(id=id)
    pessoa.delete()
    return redirect(home)