from django.shortcuts import render
from django.http import HttpResponse
from newUser import NewUserForm, UserProfileForm
from models import Person, UserProfile
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
import repDistrict

def registerUser(request):
    return render(request, 'index.html')
    
def index(request):
    if request.user.is_authenticated():
        return redirect('/home/', request)

    if request.method == 'POST':
        user_form = NewUserForm(request.POST)
        profile_form = UserProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            plainPass = user.password
            user.set_password(user.password)
            user.save()
            
            profile = profile_form.save(commit = False)
            profile.user = user
            
            stateAndDistrict = repDistrict.getRepDistrict(profile.address)
            split = stateAndDistrict.split(" ");
            profile.state = split[0].upper()
            profile.district = split[1]
            
            profile.address = ""
            
            profile.save()
            state = Person.objects.all().filter(state = profile.state)
            
            rep = Person.objects.get(state=profile.state, district=profile.district)
            sen = state.filter(district=None)
            
            
            stateString = ""
            for s in state:
                stateString += s.first_name + " " + s.last_name
            
            repString = rep.first_name + " " + rep.last_name
            
            senString = ""
            for s in sen:
                senString += s.first_name + " " + s.last_name
            #return HttpResponse("State: " + profile.state + " District: " + profile.district + " Representative: " + repString + " Senators: " + senString)
            user = authenticate(username=user.username,password=plainPass)
            login(request, user)
            return redirect('/home/', request)
    else:
        user_form = NewUserForm()
        profile_form = UserProfileForm()
        
        
    return render(request, 'index.html', {'user_form': user_form, 'profile_form' : profile_form})
    
def newUserAddress(request):
    if request.method == 'POST':
        address = request.POST.get('address', None)
        return HttpResponse(repDistrict.getRepDistrict(address))
    return HttpResponse("Not found")
    
def loginUser(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    print user
    if user:
        login(request, user)
        return redirect('/home/', request)
    else:
        return HttpResponse("User login failed")

def logoutUser(request):
    logout(request)
    return redirect('/', request)

def display_congressmen(request):
    if request.user.is_authenticated():
        profile = UserProfile.objects.get(user=request.user)
        print profile
        state = Person.objects.all().filter(state = profile.state)
        
        rep = Person.objects.get(state=profile.state, district=profile.district)
        sen = state.filter(district=None)
        
        for index, s in enumerate(sen):
            if index == 0:
                sen1 = s
            else:
                sen2 = s
        
        #return HttpResponse("State: " + profile.state + " District: " + str(profile.district) + " Representative: " + repString + " Senators: " + senString)
        return render(request, 'home.html',{'rep': rep, 'sen1' : sen1, 'sen2': sen2} )
    else:
        user_form = NewUserForm()
        profile_form = UserProfileForm()
        return render(request, 'index.html', {'user_form': user_form, 'profile_form': profile_form})
        