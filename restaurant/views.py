from django.shortcuts import render,redirect, get_object_or_404
from .models import *
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request,'index.html')

def menu(request):
    return render(request,'menu.html') 

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("myaccount"))
        else:
            return render(request, "login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("booking"))
    else:
        return render(request, "register.html")


@login_required
def booking(request):
    if request.method == "POST":
        form = BookingForm(request.POST,request.FILES)
        if form.is_valid():
            booking=form.save(commit=False)
            booking.name= request.user
           # Check for overlapping bookings
            existing_bookings = Booking.objects.filter(date=booking.date, time=booking.time)
            if existing_bookings.exists():
                messages.error(request, 'The selected date and time is already booked. Please select a different date and time.')
            else:
            # Save the booking if there are no overlaps
                booking.save()
                messages.success(request, 'Booking created successfully.')
                return redirect('myaccount')
    else:
        form = BookingForm()
    return render(request, 'booking.html', {'form': form})

@login_required
def myaccount(request):
    user = request.user
    bookings = Booking.objects.filter(name=user)
    return render(request, 'myaccount.html', {'bookings': bookings})

@login_required
def edit_booking(request,booking_id):
    booking = get_object_or_404(Booking, id=booking_id, name=request.user)
    form = BookingForm(instance=booking)
    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            # Check for overlapping bookings
            existing_bookings = Booking.objects.filter(date=form.cleaned_data['date'], time=form.cleaned_data['time'])
            for existing_booking in existing_bookings:
                if booking.id != existing_booking.id:
                    messages.error(request, 'The selected date and time is already booked. Please select a different date and time.')
                    return redirect(reverse('edit_booking', args=[booking_id]))

            # Save the booking if there are no overlaps
            form.save()
            messages.success(request, 'Booking updated successfully.')
            return redirect(reverse('myaccount'))

    context = {
        'form': form,
        'booking': booking,
    }
    return render(request, 'edit_booking.html', context)    