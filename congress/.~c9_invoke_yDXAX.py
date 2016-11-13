from django.shortcuts import render
from django.http import HttpResponse
from newUser import NewUserForm
import repDistrict


# Create your views here.

def index(request):
    return render(request, 'useraddressform.html')
    
def registerUser(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.set_password(user.password)
            
            return HttpResponse(user.email)
    else:
        user_form = NewUserForm()
        prof
        
        
    return render(request, 'register.html', {'user_form': form,})
    
def newUserAddress(request):
    if request.method == 'POST':
        address = request.POST.get('address', None)
        return HttpResponse(repDistrict.getRepDistrict(address))
    return HttpResponse("Not found")

    

