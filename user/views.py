from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import UserRegisterForm 
from django.contrib.auth.decorators import login_required
from .models import User, Profile
from event_social_network.models import Friendship
from django.db.models import Q
from event_social_network.models import Event

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST) 
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def user_profile(request, user_id):
    profile_user = get_object_or_404(User, id=user_id)
    profile, created = Profile.objects.get_or_create(user=profile_user)

    if request.user == profile_user:
        pending_friend_requests = Friendship.objects.filter(user2=profile_user, status='pending')
    else:
        pending_friend_requests = []

    friends = Friendship.objects.filter(
        (Q(user1=profile_user) | Q(user2=profile_user)) & Q(status='accepted')
    )

    # Fetch events associated with the profile user
    events = Event.objects.filter(creator=profile_user)

    return render(request, 'users/profile.html', {
        'profile_user': profile_user,
        'profile': profile,
        'pending_friend_requests': pending_friend_requests,
        'friends': friends,
        'events': events,  # Include the events in the context dictionary
    })
