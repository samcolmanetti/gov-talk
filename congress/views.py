from django.shortcuts import render
from django.http import HttpResponse
from newUser import NewUserForm, UserProfileForm
import repDistrict


# Create your views here.

def index(request):
    return render(request, 'useraddressform.html')
    
def registerUser(request):
    if request.method == 'POST':
        user_form = NewUserForm(request.POST)
        profile_form = UserProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            
            profile = profile_form.save(commit = False)
            profile.user = user
            
            
            
            return HttpResponse(repDistrict.getRepDistrict(profile.address))
    else:
        user_form = NewUserForm()
        profile_form = UserProfileForm()
        
        
    return render(request, 'register.html', {'user_form': user_form, 'profile_form' : profile_form})
    
def newUserAddress(request):
    if request.method == 'POST':
        address = request.POST.get('address', None)
        return HttpResponse(repDistrict.getRepDistrict(address))
    return HttpResponse("Not found")

    

