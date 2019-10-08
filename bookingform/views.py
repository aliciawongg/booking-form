from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import customerBooking
# Create your views here.
def displayForm(request):
    return render(request,'booking.html')    

def submitBooking(request):
    new_booking = customerBooking(content = request.POST['content'])
    new_booking.save()
    return render('submitted')
