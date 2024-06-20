from django.shortcuts import render, get_object_or_404
from .models import Service

def index(request):
    latest_services = Service.objects.all()[:3]  # Get the latest 3 services
    return render(request, 'main/index.html', {'latest_services': latest_services})

def service_list(request):
    services = Service.objects.all()
    return render(request, 'main/service_list.html', {'services': services})

def service_detail(request, slug):
    service = get_object_or_404(Service, slug=slug)
    return render(request, 'main/service_detail.html', {'service': service})

