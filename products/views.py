import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.shortcuts import get_object_or_404
from .models import Product

@csrf_exempt
@require_http_methods(["POST"])
def create_product(request):
    try:
        data = json.loads(request.body)
        product = Product.objects.create(
            name=data['name'],
            description=data.get('description', ''),
            price=data['price'],
            stock=data['stock'],
            is_available=data.get('is_available', True)
        )
        return JsonResponse({'id': product.id, 'name': product.name, 'description': product.description, 'price': float(product.price), 'stock': product.stock, 'is_available': product.is_available}, status=201)
    except (KeyError, json.JSONDecodeError, ValueError) as e:
        return JsonResponse({'error': str(e)}, status=400)

@csrf_exempt
@require_http_methods(["POST", "PUT"])
def update_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    try:
        data = json.loads(request.body)
        product.name = data.get('name', product.name)
        product.description = data.get('description', product.description)
        product.price = data.get('price', product.price)
        product.stock = data.get('stock', product.stock)
        product.is_available = data.get('is_available', product.is_available)
        product.save()
        return JsonResponse({'id': product.id, 'name': product.name, 'description': product.description, 'price': float(product.price), 'stock': product.stock, 'is_available': product.is_available})
    except (json.JSONDecodeError, ValueError) as e:
        return JsonResponse({'error': str(e)}, status=400)

@csrf_exempt
@require_http_methods(["DELETE", "PUT"])
def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.delete()
    return JsonResponse({'message': 'Producto eliminado correctamente'}, status=200)

def list_products(request):
    products = Product.objects.all()
    data = [{'id': p.id, 'name': p.name, 'price': float(p.price), 'stock': p.stock, 'is_available': p.is_available} for p in products]
    return JsonResponse(data, safe=False)