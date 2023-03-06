from django.shortcuts import render

# Create your views here.


def get_homepage(request):
    return render(request, '../templates/index.html')


def get_admin_page(request):
    return render(request, '../templates/admin_page.html')
