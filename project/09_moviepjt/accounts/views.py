from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods, require_POST
from .models import User

from .forms import UserCustomCreationForm


# Create your views here.
@require_http_methods(["GET", "POST"])
def signup(request):
    if request.user.is_authenticated:
        return redirect('movies:list')
    if request.method == 'POST':
        user_form = UserCustomCreationForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            auth_login(request, user)
            return redirect('movies:list')
    else:
        user_form = UserCustomCreationForm()
    context = {
        'form': user_form,
        'sign': "up",
    }
    return render(request, 'accounts/forms.html', context)

def login(request):
    if request.user.is_authenticated:
        return redirect('movies:list')
    if request.method == 'POST':
        login_form = AuthenticationForm(request, request.POST)
        if login_form.is_valid():
            auth_login(request, login_form.get_user())
            return redirect('movies:list')
    else:
        login_form = AuthenticationForm()
    context = {
        'form': login_form,
        'sign': "in",
    }
    return render(request, 'accounts/forms.html', context)

@login_required
def logout(request):
    auth_logout(request)
    return redirect('movies:list')
    
@login_required
def user_list(request):
    users = User.objects.all()
    context = {
        'users': users,
    }
    return render(request, 'accounts/userlist.html', context)
    
def people(request, user_id):
    people = get_object_or_404(User, id=user_id)
    followers_count = people.followers.count()
    followings_count = people.followings.count()
    scores = people.score_set.all()
    context = {
        'people':people,
        'scores':scores,
        'followings_count':followings_count,
        'followers_count':followers_count
    }
    
    return render(request, 'accounts/people.html', context)
    
def follow(request, user_id):
    person = get_object_or_404(User, pk=user_id) # 내가 팔로우 하고자 하는 사람
    
    # 만약 현재 유저가 해당 유저를 이미 팔로우하고 있었으면,
    if request.user in person.followings.all(): # 내가 person의 팔로워들 중에 있으면
        #   ---> 팔로우 취소
        request.user.followers.remove(person)
        person.followings.remove(request.user)
        # 아니면,
    else:
        #   ---> 팔로우
        request.user.followers.add(person)
        person.followings.add(request.user)
    return redirect('accounts:people', person.id)
    
    
@login_required
def followings(request, user_id):
    people = get_object_or_404(User, id=user_id)
    following_users = people.followings.all()
    context = {
        'follow_users': following_users,
    }
    return render(request, 'accounts/followlist.html', context)
    
@login_required
def followers(request, user_id):
    people = get_object_or_404(User, id=user_id)
    follower_users = people.followers.all()
    context = {
        'follow_users': follower_users,
    }
    return render(request, 'accounts/followlist.html', context)