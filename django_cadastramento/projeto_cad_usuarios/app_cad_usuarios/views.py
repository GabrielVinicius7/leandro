from django.shortcuts import render
from .models import Usuario



def home(request):
    return render(request,'usuarios/home.html')

def usuarios(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        idade = request.POST.get('idade')

        # Este if abaixo foi feito para que o botão (cadastrados), na tela home funcionasse
        if nome and idade:  # Verifica se os campos estão preenchidos
            novo_usuario = Usuario(nome=nome, idade=idade)
            novo_usuario.save()

    # Exibir todos os usuários já cadastrados em uma nova página
    usuarios = {
        'usuarios': Usuario.objects.all()
    }

    # Retornar os dados para a página de listagem de usuários
    return render(request,'usuarios/usuarios.html',usuarios)