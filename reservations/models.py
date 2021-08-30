from django.db import models
from django.utils.timezone import now
from rest_framework.reverse import reverse


class Room(models.Model):
    name = models.CharField(max_length=120, unique=True)
    places = models.IntegerField(default=0)
    monitor = models.BooleanField(default=False)
    owner = models.ForeignKey(
        'auth.User', related_name='rooms', on_delete=models.CASCADE)

    class Meta:
        ordering = ['places']

    def __str__(self) -> str:
        return f'{self.name}, {self.places}, {self.monitor}'

    def get_absolute_url(self):
        return reverse('room', args=[str(self.id)])


class Reservation(models.Model):
    title = models.CharField(max_length=120, default='Reservation')
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    date_from = models.DateTimeField(default=now)
    date_to = models.DateTimeField(default=now)
    employees = models.CharField(max_length=200, default=None)
    created = models.DateTimeField(default=now, editable=False)
    cancel = models.BooleanField(default=False)
    owner = models.ForeignKey(
        'auth.User', related_name='reservations', on_delete=models.CASCADE)

    class Meta:
        ordering = ['date_from', 'date_to']

    def __str__(self) -> str:
        return f'{self.title}, {self.room}, {self.date_from}, {self.date_to}, \
        {self.cancel}'

    def get_absolute_url(self):
        return reverse('reservation', args=[str(self.id)])
