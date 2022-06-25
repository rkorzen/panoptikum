from django.shortcuts import render

# Create your views here.
from photos.models import Gallery


def galleries_list(request):
    galleries = Gallery.objects.all()
    return render(
        request,
        'photos/list.html',
        {"galleries": galleries}
    )