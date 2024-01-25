from django.shortcuts import render
from .models import Travelpackage

# Create your views here.
def package_list(request):
    packages = Travelpackage.objects.all()
    return render(request, 'travel/package_list.html', {'packages': packages})