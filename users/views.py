from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserProfileForm


def register(request):
    if request.POST:
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request,f'Welcome {username}, account is created')
            return redirect('/food/')
        else:
            messages.error(request,'Try Again')
    form=UserCreationForm()
    return render(request,'users/register.html',{'form':form})

@login_required
def profile(request):
    return render(request,'users/profile.html')


@login_required
def profile_update(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Kullanıcının profil sayfasına yönlendirme
    else:
        form = UserProfileForm(instance=request.user.profile)
    
    return render(request, 'users/profile_update.html', {'form': form})