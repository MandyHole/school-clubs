from django.shortcuts import render

# Create your views here.


def get_homepage(request):
    return render(request, '../templates/index.html')


def get_admin_page(request):
    return render(request, '../templates/admin_page.html')


def get_manage_booking(request):
    return render(request, '../templates/manage_bookings.html')


def get_make_booking(request):
    return render(request, '../templates/book_new.html')