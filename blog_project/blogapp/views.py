from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Image

def home_page(request):
    p_image = Image.objects.first()

    context = {
        "images": p_image
    }
    return render(request, "index.html", context)
