from .models import Reservation
from django.db.models import Q


def check_data(request, pk=None):
    room = request.data['room']
    date_to = request.data['date_to']
    date_from = request.data['date_from']

    reservation = Reservation.objects.filter(
        (Q(date_to__range=[date_from, date_to]) |
         Q(date_from__range=[date_from, date_to])) &
        Q(room=room) & Q(cancel=False) & ~Q(id=pk)
    )

    if reservation:
        return False
    else:
        return True
