from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic, View
from .models import BookClub, Breakfast, Parent, Pupil
from django.contrib.auth.models import User
from .forms import PupilForm

# Create your views here.


def get_homepage(request):
    return render(request, '../templates/index.html')


def get_admin_page(request):
    return render(request, '../templates/admin_page.html')


def get_manage_booking(request):
    pupils = Pupil.objects.all()
    parents = Parent.objects.all()
    users = User.objects.all()

    context = {
        'pupils': pupils,
        'parents': parents,
        'users': users
    }

    return render(request, '../templates/manage_bookings.html', context)


def get_make_booking(request):
    return render(request, '../templates/book_new.html')


# def add_pupil(request):
#     if request.method == 'POST':
#         first_name = request.POST.get('pupil_first_name')
#         surname = request.POST.get('pupil_surname')
#         year_group = 'pupil_year_group' in request.POST

#         Pupil.objects.create(
#             first_name_of_pupil=first_name, 
#             surname_of_pupil=surname, year_gp=year_group)

#         return redirect('get_manage_booking')
#     # pupils = Pupil.objects.all()
#     # context = {
#     #     'pupils': pupils,
#     # }

#     return render(request, '../templates/add_pupil.html')

def add_pupil(request):
    if request.method == 'POST':
        form = PupilForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('get_homepage')
    form = PupilForm()
    context = {
        'form': form
    }
    return render(request, '../templates/add_pupil.html', context)


class AddPupil(View):

    def get(self, request, *args, **kwargs):
        # queryset = Pupil.objects.all
        # post = get_object_or_404()
        # comments = post.comments.filter(approved=True).order_by("-created_on")
        # liked = False
        # if post.likes.filter(id=self.request.user.id).exists():
        #     liked = True

        return render(
            request, 
            '../templates/add_pupil.html',
            {
                "add_pupil_form": PupilForm()
            },
        )
    
    def post(self, request, *args, **kwargs):

        # queryset = Pupil.objects.all
        # post = get_object_or_404(queryset)

        add_pupil_form = PupilForm(data=request.POST)
        if add_pupil_form.is_valid():
            # add_pupil_form.instance.email = request.user.email
            # add_pupil_form.instance.name = request.user.username
            # add_pupil_form.instance.first_name_of_pupil = request.user.first_name_of_pupil
            # add_pupil_form.instance.surname_of_pupil = request.user.surname_of_pupil
            # add_pupil_form.instance.year_gp = request.user.year_gp
            pupil = add_pupil_form.save(commit=False)
            # pupil.post = post
            pupil.save()
        else:
            add_pupil_form = PupilForm()

        return render(
            request, 
            '../templates/add_pupil.html',
            {
                "add_pupil_form": PupilForm()
            },
        )

