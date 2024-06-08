from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Room

def initiate_call(request):
    """Creates a new room for video consultation and returns the room name."""
    if request.method == 'POST':
        room_name = request.POST.get('room_name')
        room = Room.objects.create(name=room_name)
        return JsonResponse({'room_name': room.name})
    return JsonResponse({'error': 'Invalid request method'}, status=400)

def join_call(request, room_name):
    """Checks if the room exists and returns the room name."""
    room = get_object_or_404(Room, name=room_name)
    return JsonResponse({'room_name': room.name})

def leave_call(request, room_name):
    """Deletes the room after the call is finished."""
    room = get_object_or_404(Room, name=room_name)
    room.delete()
    return JsonResponse({'message': 'Left the call successfully'})
