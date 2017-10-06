from django.shortcuts import render
from base_app.forms import UserForm, UserProfileInfoForm

#for login
from django.contrib.auth import authenticate, login,logout
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    return render(request,'base_app/index.html')

@login_required
def special(request):
    return HttpResponse("you are logged in, Nice!")

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def register(request): #registrationpage
    registered = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

#            if 'profile_pic' in request.FILES:
#                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request,'base_app/registration.html',{'user_form':user_form,'profile_form':profile_form,'registered':registered})



def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user is not None:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('userdash')) #after login where?
            else:
                return HttpResponse("ACCOUNT NOT ACTIVE")
        else:
            print("Someone Tried to login and failed!")
            print("Username: {} and password {}".format(username,password))
            return HttpResponse("invalid login details supplied!")
    else:
        return render(request,'base_app/login.html',{})

def userdash(request):
    return render(request,'base_app/userdash.html')


def admins_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user is not None:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('adminspage')) #after login where?
            else:
                return HttpResponse("ACCOUNT NOT ACTIVE")
        else:
            print("Someone Tried to login and failed!")
            print("Username: {} and password {}".format(username,password))
            return HttpResponse("invalid login details supplied!")
    else:
        return render(request,'base_app/admins.html',{})


def adminspage(request):
    return render(request,'base_app/adminspage.html')




def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('userdash')) #after login where?
            else:
                return HttpResponse("ACCOUNT NOT ACTIVE")
        else:
            print("Someone Tried to login and failed!")
            print("Username: {} and password {}".format(username,password))
            return HttpResponse("invalid login details supplied!")
    else:
        return render(request,'base_app/login.html',{})

# def add_item(request):
#     form = SongForm(request.POST or None, request.FILES or None)
#     if form.is_valid():
#         productinfos = ProductInfo_set.all()
#         for s in productinfos:
#             if s.ProductInfo_name == form.cleaned_data.get("ProductInfo_name"):
#                 context = {
#                     'info': info,
#                     'form': form,
#                     'error_message': 'You already added that song',
#                 }
#                 return render(request, 'base_app/adminspage.html', context)
#         ProductInfo = form.save(commit=False)
#         if 'profile_pic' in request.FILES:
#             productinfos.images = request.FILES['images']
#             return render(request, 'base_app/adminspage.html')
#
#         productinfos.save()
#         return render(request, 'music/detail.html', {'info': info})
#     context = {
#         'info': info,
#         'form': form,
#     }
#     return render(request, 'base_app/adminspage.html', context)
