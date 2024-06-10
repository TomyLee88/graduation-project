from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseForbidden
from .forms import EventForm
from .forms import UserSearchForm
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Event, Friendship
from user import views
from django.http import HttpResponseForbidden

def home(request):
    events = Event.objects.all()
    return render(request, 'event_social_network/home.html', {'events': events})

def about(request):
    return render(request, 'event_social_network/about.html')

@login_required
def create_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.creator = request.user
            event.save()
            return redirect('home')
    else:
        form = EventForm()
    return render(request, 'event_social_network/create_event.html', {'form': form})

def all_events(request):
    events = Event.objects.all()
    return render(request, 'event_social_network/events_list.html', {'events': events})

@login_required
def user_search(request):
    if request.method == 'GET':
        form = UserSearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data.get('query')
            
            # perform search query for users and also events
            user_results = User.objects.filter(username__icontains=query)
            event_results = Event.objects.filter(Q(title__icontains=query) | Q(description__icontains=query))
            
            # prepare user search results and also skip adding the current user to the search results
            user_search_results = []
            for user in user_results:
                if user == request.user:
                    continue 
                
                friendship = Friendship.objects.filter(user1=request.user, user2=user).first()
                
                if not friendship:
                    friendship_status = 'not_friends'
                    friendship_id = None
                else:
                    friendship_status = friendship.status
                    friendship_id = friendship.id
                
                user_search_results.append((user, friendship_status, friendship_id))
            
            return render(request, 'event_social_network/search_results.html', {
                'user_search_results': user_search_results, 
                'event_results': event_results,
                'query': query
            })
    else:
        form = UserSearchForm()
    return render(request, 'event_social_network/user_search.html', {'form': form})

def event_details(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    return render(request, 'event_social_network/event_details.html', {'event': event})

@login_required
def edit_event(request, event_id):
    event = get_object_or_404(Event, id=event_id, creator=request.user)
    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = EventForm(instance=event)
    return render(request, 'event_social_network/edit_event.html', {'form': form})

@login_required
def delete_event(request, event_id):
    event = get_object_or_404(Event, id=event_id, creator=request.user)
    if request.method == 'POST':
        event.delete()
        return redirect('home')
    return render(request, 'event_social_network/delete_event.html', {'event': event})
@login_required
def send_friend_request(request, recipient_id):
    recipient = get_object_or_404(User, id=recipient_id)

    # check if a friendship request already exists between the sender and recipient
    existing_request = Friendship.objects.filter(user1=request.user, user2=recipient).exists()

    # check if sender is not trying to send a friend request to themselves if not than create a pending friendship request
    if request.user != recipient and not existing_request:

        Friendship.objects.create(user1=request.user, user2=recipient, status='pending')
        
    return redirect('user_profile', user_id=recipient_id)
@login_required
def cancel_friend_request(request, friendship_id):
    friendship = get_object_or_404(Friendship, id=friendship_id)
    # check if the current user is the sender of the friend request and if status is pending
    if request.user == friendship.user1 and friendship.status == 'pending':
        friendship.delete()
    # redirect to the profile page of the current user
    return redirect('user_profile', user_id=request.user.id)

@login_required
def accept_friend_request(request, friendship_id):
    friendship = get_object_or_404(Friendship, id=friendship_id)
    if request.user == friendship.user2 and friendship.status == 'pending':
        friendship.status = 'accepted'
        friendship.save()
        return redirect('user_profile', user_id=request.user.id)
    else:
        return HttpResponseForbidden("You are not allowed to accept this friend request.")


@login_required
def reject_friend_request(request, friendship_id):
    friendship = get_object_or_404(Friendship, id=friendship_id)
    if request.user == friendship.user2 and friendship.status == 'pending':
        friendship.delete()
        return redirect('user_profile', user_id=request.user.id)
    else:
        return HttpResponseForbidden("You are not allowed to reject this friend request.")
    

@login_required
def remove_friend(request, friendship_id):
    friendship = get_object_or_404(Friendship, id=friendship_id)
    if friendship.user1 == request.user or friendship.user2 == request.user:
        friendship.delete()
        return redirect('user_profile', user_id=request.user.id)
    else:
        return HttpResponseForbidden("You are not allowed to remove this friend.")


