from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic, View
from .models import Pupil, DateRequest
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import PupilForm, DateRequestForm, EditPupilForm
from datetime import date
from django.views.generic.edit import CreateView


def get_homepage(request):
    return render(request, '../templates/index.html')


def get_manage_booking(request):
    pupils = Pupil.objects.all()
    users = User.objects.all()
    date_requests = DateRequest.objects.all()

    context = {
        'pupils': pupils,
        'users': users,
        'date_requests': date_requests
    }

    return render(request, '../templates/manage_bookings.html', context)


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

        pupil_form = PupilForm(data=request.POST)
        if pupil_form.is_valid():
            pupil_form.instance.contact_email_for_pupil = request.user.email
            pupil_form.instance.user_info = request.user
            pupil = pupil_form.save(commit=False)
            pupil.save()
            messages.success(
                request,
                'Your child has been added successfully.')
            return redirect('get_manage_booking')
        else:
            messages.error(
                request,
                'Please confirm you understand the charges')
            return render(
                request,
                '../templates/add_pupil.html',
                {
                    "add_pupil_form": pupil_form
                },
            )


def edit_pupil(request, pupil_id):
    pupil = get_object_or_404(Pupil, id=pupil_id)
    users = User.objects.all()
    if request.method == 'POST':
        form = EditPupilForm(request.POST, instance=pupil)
        if form.is_valid():
            form.instance.booking_approval_status = '0'
            form.save()
            messages.success(
                request,
                'Your requested amendments have been received successfully.')
            return redirect('get_manage_booking')
    form = EditPupilForm(instance=pupil)
    context = {
        'form': form,
        'pupil': pupil,
        'users': users
    }
    return render(request, '../templates/amend_pupil.html', context)


def delete_date(request, cancel_id):
    cancel = get_object_or_404(DateRequest, id=cancel_id)
    cancel.delete()
    return redirect('get_manage_booking')


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
            messages.success(
                request,
                'Your date request has been submitted successfully.')
            return redirect('get_manage_booking')
        else:
            messages.warning(
                request,
                'Please try again with the date in the correct format')

    date_form = DateRequestForm(instance=pupil)
    context = {
        'date_form': date_form,
        'pupil': pupil
    }
    return render(request, '../templates/date_request.html', context)
