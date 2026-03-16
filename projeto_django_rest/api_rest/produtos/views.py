from django.shortcuts import render
from django.http import JsonResponse
from .models import Produto
from django.views.decorators.csrf import csrf_exempt
import json


@csrf_exempt
def lista_produtos(request):

    if request.method == 'GET':
        produtos = list(Produto.objects.values())
        return JsonResponse(produtos, safe=False)

    if request.method == 'POST':
        dados = json.loads(request.body)
        produto = Produto.objects.create(
            nome=dados['nome'],
            preco=dados['preco']
        )
        return JsonResponse({"id": produto.id})


@csrf_exempt
def detalhe_produto(request, id):

    produto = Produto.objects.get(id=id)

    if request.method == 'PUT':
        dados = json.loads(request.body)
        produto.nome = dados['nome']
        produto.preco = dados['preco']
        produto.save()
        return JsonResponse({"status": "alterado"})

    if request.method == 'DELETE':
        produto.delete()
        return JsonResponse({"status": "apagado"})

# Create your views here.
