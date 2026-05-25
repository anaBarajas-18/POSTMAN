from django.http import JsonResponse
from .models import Dog

def dogs_list(request):
    # Obtener todos los perritos, aplicar filtros si vienen en la query
    queryset = Dog.objects.all()
    
    min_age = request.GET.get('min_age')
    if min_age:
        queryset = queryset.filter(age__gte=min_age)
    max_age = request.GET.get('max_age')
    if max_age:
        queryset = queryset.filter(age__lte=max_age)
    
    vaccinated = request.GET.get('vaccinated')
    if vaccinated:
        if vaccinated.lower() == 'true':
            queryset = queryset.filter(vaccinated=True)
        elif vaccinated.lower() == 'false':
            queryset = queryset.filter(vaccinated=False)
    
    size = request.GET.get('size')
    if size:
        queryset = queryset.filter(size=size)
    
    adopted = request.GET.get('adopted')
    if adopted:
        if adopted.lower() == 'true':
            queryset = queryset.filter(adopted=True)
        elif adopted.lower() == 'false':
            queryset = queryset.filter(adopted=False)
    
    ordering = request.GET.get('ordering')
    if ordering:
        queryset = queryset.order_by(ordering)
    
    data = list(queryset.values())
    # Convertir Decimal a float para JSON (si hay campos weight)
    for item in data:
        if 'weight' in item and item['weight'] is not None:
            item['weight'] = float(item['weight'])
    
    return JsonResponse({
        "message": "Dogs retrieved successfully",
        "total": len(data),
        "data": data
    }, status=200)

def dog_detail(request, pk):
    try:
        dog = Dog.objects.get(pk=pk)
        data = {
            'id': dog.id,
            'name': dog.name,
            'breed': dog.breed,
            'age': dog.age,
            'size': dog.size,
            'weight': float(dog.weight) if dog.weight else None,
            'color': dog.color,
            'vaccinated': dog.vaccinated,
            'adopted': dog.adopted,
            'energy': dog.energy,
            'gender': dog.gender,
        }
        return JsonResponse({
            "message": "Dog retrieved successfully",
            "total": 1,
            "data": data
        }, status=200)
    except Dog.DoesNotExist:
        return JsonResponse({"error": f"Perrito con ID {pk} no encontrado"}, status=404)

def dogs_by_breed(request, breed):
    dogs = Dog.objects.filter(breed__iexact=breed)
    data = list(dogs.values())
    for item in data:
        if 'weight' in item and item['weight'] is not None:
            item['weight'] = float(item['weight'])
    return JsonResponse({
        "message": f"Dogs of breed {breed}",
        "total": len(data),
        "data": data
    }, status=200)

def dogs_search(request, query):
    dogs = Dog.objects.filter(name__icontains=query)
    data = list(dogs.values())
    for item in data:
        if 'weight' in item and item['weight'] is not None:
            item['weight'] = float(item['weight'])
    return JsonResponse({
        "message": f"Results for '{query}'",
        "total": len(data),
        "data": data
    }, status=200)

def adoptable_dogs(request):
    dogs = Dog.objects.filter(adopted=False, vaccinated=True)
    data = list(dogs.values())
    for item in data:
        if 'weight' in item and item['weight'] is not None:
            item['weight'] = float(item['weight'])
    return JsonResponse({
        "message": "Perritos disponibles para adopción",
        "total": len(data),
        "data": data
    }, status=200)

def puppies(request):
    dogs = Dog.objects.filter(age__lt=2)
    data = list(dogs.values())
    for item in data:
        if 'weight' in item and item['weight'] is not None:
            item['weight'] = float(item['weight'])
    return JsonResponse({
        "message": "Cachorritos",
        "total": len(data),
        "data": data
    }, status=200)