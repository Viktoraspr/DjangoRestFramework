from django.urls import path

from .views import (ReservationDetail, ReservationList, RoomDetail, RoomsList,
                    UserDetail, UserList, api_root)

urlpatterns = [
    path('', api_root),
    path('rooms/', RoomsList.as_view(), name='rooms'),
    path('rooms/<int:pk>/', RoomDetail.as_view(), name="room"),
    path('reservations/', ReservationList.as_view(), name="reservations"),
    path('reservations/<int:pk>/', ReservationDetail.as_view(),
         name="reservation"),
    path('users/', UserList.as_view(), name='user-list'),
    path('users/<int:pk>/', UserDetail.as_view(), name='user-detail'),
]
