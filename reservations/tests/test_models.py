from django.test import TestCase
from django.contrib.auth import get_user_model
from ..models import Room, Reservation

User = get_user_model()


class ProductTestCase(TestCase):

    def setUp(self):  # Python's builtin unittest
        user = User.objects.create_user(
            'user_2', 'cfe3@invlalid.com', 'some_123_password')
        self.user = user
        Room.objects.create(name="Melynas",
                            places=30, monitor=True, owner=self.user)
        self.room = Room.objects.get(id=1)
        Reservation.objects.create(title='Meeting with sales persons',
                                   room=self.room, date_from='2021-09-01T09:00:00Z',
                                   date_to='2021-09-01T10:00:00Z',
                                   employees="Jonas, Petras, Antanas",
                                   cancel=False,
                                   owner=self.user)
        self.reservation = Reservation.objects.get(id=1)

    def test_reservation_get_absolute_url(self):
        reservation = Reservation.objects.get(id=1)
        self.assertEqual(reservation.get_absolute_url(), '/reservations/1/')

    def test_room_get_absolute_url(self):
        reservation = Room.objects.get(id=1)
        self.assertEqual(reservation.get_absolute_url(), '/rooms/1/')
