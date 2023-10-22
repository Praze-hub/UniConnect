from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from .models import Profile, Post, Comment
from django.contrib.auth.decorators import login_required
from .models import Profile
from .forms import ProfileEditForm
from django.contrib import messages



# Create your views here.
@login_required
def profile(request, username):
    user = get_object_or_404(User, username=username)
    profile = Profile.objects.get(user=user)
    posts = Post.objects.filter(user = user)
    # followers = profile.followers.count()
    # following = profile.user.following.count()

    context = {'user':user, 'profile':profile, 'posts':posts}
    return render(request, 'profile.html',context)

def post_detail(request, post_id):
    pass

@login_required
def edit(request):
    if request.method == 'POST':
        profile_form = ProfileEditForm(
            instance=request.user.profile,
            data = request.POST,
            files = request.FILES
        )
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request,'Error updating your profile')
    else:
        profile_form = ProfileEditForm(
            instance=request.user.profile
        )

    return render(request,'edit.html',{'profile_form':profile_form})

    
    


