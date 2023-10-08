from django.core.paginator import Paginator
from django.shortcuts import render
from . import models 
# Create your views here.

def all_rooms(request):
    page = request.GET.get('page')
    room_list = models.Room.objects.all()
    paginator = Paginator(room_list, per_page=10)
    rooms_on_page = paginator.get_page(page)
    
    return render(
        request, 
        template_name="rooms/home.html",
        context={
            'rooms': rooms_on_page
    })
