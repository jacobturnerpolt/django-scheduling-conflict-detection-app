from django.shortcuts import render
from .models import Booking
from .forms import BookingForm

def make_booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            resource = form.cleaned_data['resource']
            start_time = form.cleaned_data['start_time']
            end_time = form.cleaned_data['end_time']

            conflicts = Booking.get_conflicts(resource, start_time, end_time)

            if conflicts.exists():
                return render(request, 'make_booking.html', {
                    'form': form,
                    'conflicts': conflicts
                })
            else:
                form.save()
                return render(request, 'make_booking.html', {
                    'form': BookingForm(),
                    'success': True
                })
    else:
        form = BookingForm()
        return render(request, 'make_booking.html', {'form': form})