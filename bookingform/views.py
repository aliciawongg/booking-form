from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import customerBooking
from .forms import customerBookingForm
# Create your views here.
# def displayForm(request):
#     return render(request,'booking.html')    

def submitBooking(request):
    form = customerBookingForm()
    if request.method == "POST":
        form = customerBookingForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'notification.html')
    return render(request,'booking.html', {'form': form})

def showAllBookings(request):
    all_bookings = customerBooking.objects.all()
    return render(request, 'listbookings.html', 
        {'all_bookings': all_bookings})