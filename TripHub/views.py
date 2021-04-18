from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def guide(request):
    return render(request, 'guides_page.html')
