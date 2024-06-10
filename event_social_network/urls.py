from django.urls import path
from event_social_network import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('create/', views.create_event, name='create_event'),
    path('search/', views.user_search, name='user_search'),
    path('event/<int:event_id>/', views.event_details, name='event_details'),
    path('events/', views.all_events, name='all_events'),
    path('event/<int:event_id>/delete/', views.delete_event, name='delete_event'),
    path('event/<int:event_id>/edit/', views.edit_event, name='edit_event'),
    path('send_friend_request/<int:recipient_id>/', views.send_friend_request, name='send_friend_request'),
    path('cancel_friend_request/<int:friendship_id>/', views.cancel_friend_request, name='cancel_friend_request'),
    path('accept_friend_request/<int:friendship_id>/', views.accept_friend_request, name='accept_friend_request'),
    path('remove_friend/<int:friendship_id>/', views.remove_friend, name='remove_friend'),
    path('reject_friend_request/<int:friendship_id>/', views.reject_friend_request, name='reject_friend_request'),
]
