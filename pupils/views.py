from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic, View
from .models import BookClub, Breakfast, Parent, Pupil
from django.contrib.auth.models import User
from .forms import PupilForm, ParentForm, EditParentForm

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
        return render(
            request, 
            '../templates/add_pupil.html',
            {
                "add_pupil_form": PupilForm()
            },
        )
    
    def post(self, request, *args, **kwargs):

        add_pupil_form = PupilForm(data=request.POST)
        if add_pupil_form.is_valid():
            add_pupil_form.instance.contact_email_for_pupil = request.user.email
            add_pupil_form.instance.user_info = request.user
            pupil = add_pupil_form.save(commit=False)
            pupil.save()
        else:
            add_pupil_form = PupilForm()

        return render(
            request,
            '../templates/manage_bookings.html',
            {
                "add_pupil_form": PupilForm()
            },
        )


class AddParent(View):

    def get(self, request, *args, **kwargs):
        return render(
            request, 
            '../templates/add_parent.html',
            {
                "add_parent_form": ParentForm()
            },
        )

    def post(self, request, *args, **kwargs):
        add_parent_form = ParentForm(data=request.POST)
        if add_parent_form.is_valid():
            add_parent_form.instance.parent_email = request.user.email
            add_parent_form.instance.user_info = request.user
            parent = add_parent_form.save(commit=False)
            # pupil.post = post
            parent.save()
        else:
            add_parent_form = ParentForm()

        return render(
            request, 
            '../templates/manage_bookings.html',
            {
                "add_parent_form": ParentForm()
            },
        )


def edit_parent(request, parent_id):
    pupils = Pupil.objects.all()
    parents = Parent.objects.all()
    users = User.objects.all()
    context = {
        'pupils': pupils,
        'parents': parents,
        'users': users
    }
    parent = get_object_or_404(Parent, id=parent_id)
    # if parent_id == Parent.user_info:
    if request.method == 'POST':
        form = EditParentForm(request.POST, instance=parent)
        if form.is_valid():
            form.save()
            return redirect('new_booking')
    form = EditParentForm(instance=parent)
    context = {
        'pupils': pupils,
        'parents': parents,
        'users': users,
        'form': form,
        'parent_id': parent_id
    }
    return render(request, '../templates/amend_parent.html', context)


def edit_pupil(request, pupil_id):
    pupil = get_object_or_404(Pupil, id=pupil_id)
    if request.method == 'POST':
        form = PupilForm(request.POST, instance=pupil)
        if form.is_valid():
            form.save()
            return redirect('new_booking')
    form = PupilForm(instance=pupil)
    context = {
        'form': form
    }
    return render(request, '../templates/amend_pupil.html', context)


def delete_pupil(request, pupil_id):
    pupil = get_object_or_404(Pupil, id=pupil_id)
    pupil.delete()
    return redirect('get_manage_booking')
