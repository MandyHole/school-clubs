from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic, View
from .models import Parent, Pupil, DateRequest, Breakfast, BreakfastRequest
from django.contrib.auth.models import User
from .forms import PupilForm, ParentForm, EditParentForm, DateRequestForm, SetBreakfastDates, EditPupilForm
from datetime import date
from django.views.generic.edit import CreateView

# Create your views here.


def get_homepage(request):
    return render(request, '../templates/index.html')


def get_manage_booking(request):
    pupils = Pupil.objects.all()
    parents = Parent.objects.all()
    users = User.objects.all()
    date_requests = DateRequest.objects.all()

    context = {
        'pupils': pupils,
        'parents': parents,
        'users': users,
        'date_requests': date_requests
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
            # add_pupil_form.instance.parent_info = request
            pupil = add_pupil_form.save(commit=False)
            pupil.save()
            return redirect('get_manage_booking')
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
    users = User.objects.all()
    if request.method == 'POST':
        form = EditPupilForm(request.POST, instance=pupil)
        if form.is_valid():
            form.instance.booking_approval_status = '0'
            form.save()
            return redirect('get_manage_booking')
    form = EditPupilForm(instance=pupil)
    parents = Parent.objects.all()
    context = {
        'form': form,
        'pupil': pupil,
        'parents': parents,
        'users': users
    }
    return render(request, '../templates/amend_pupil.html', context)


def delete_pupil(request, pupil_id):
    pupil = get_object_or_404(Pupil, id=pupil_id)
    pupil.delete()
    return redirect('get_manage_booking')


class AdminPage(View):

    def get(self, request, *args, **kwargs):
        return render(
            request,
            '../templates/admin_page.html',
            {
                "set_breakfast_date_form": SetBreakfastDates()
            },
        )

    def post(self, request, *args, **kwargs):
        set_breakfast_date_form = SetBreakfastDates(data=request.POST)
        if set_breakfast_date_form.is_valid():
            # set_breakfast_date_form.instance.breakfast_option = date.today()
            newdates = set_breakfast_date_form.save(commit=False)
            newdates.save()
        else:
            set_breakfast_date_form = SetBreakfastDates()

        return render(
            request,
            '../templates/admin_page.html',
            {
                "set_breakfast_date_form": SetBreakfastDates()
            },
        )


def breakfast_request(request, pupil_id):
    pupils = Pupil.objects.all()
    context = {
        'pupils': pupils,
    }
    pupil = get_object_or_404(Pupil, id=pupil_id)
    if request.method == 'POST':
        breakfast_form = BreakfastRequestForm(request.POST)
        if breakfast_form.is_valid():
            breakfast_form.instance.pupil = pupil
            breakfast_form.save()
            return redirect('get_manage_booking')

    breakfast_form = BreakfastRequestForm(instance=pupil)
    context = {
        'breakfast_form': breakfast_form,
        'pupil': pupil
    }
    return render(request, '../templates/breakfast_request.html', context)


def date_request(request, pupil_id):
    pupils = Pupil.objects.all()
    context = {
        'pupils': pupils,
    }
    pupil = get_object_or_404(Pupil, id=pupil_id)
    if request.method == 'POST':
        date_form = DateRequestForm(request.POST)
        if date_form.is_valid():
            date_form.instance.pupil = pupil
            date_form.save()
            return redirect('get_manage_booking')

    date_form = DateRequestForm(instance=pupil)
    context = {
        'date_form': date_form,
        'pupil': pupil
    }
    return render(request, '../templates/date_request.html', context)


class DateCreateView(CreateView):
    model = DateRequest()
    form_class = DateRequestForm
