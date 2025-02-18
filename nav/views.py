from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def map_view(request):
    return render(request, 'map.html')

def rooms(request):
    return render(request, 'rooms.html')

def room_view(request, room_number):
    return render(request, 'room.html', {'room_number': room_number})