from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def guide(request):
    return render(request, 'guides_page.html')


def guide_1(request):
    return render(request, 'guide1_page.html')


def guide_2(request):
    return render(request, 'guide2_page.html')
