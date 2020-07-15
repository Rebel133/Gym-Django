from django.shortcuts import render, HttpResponse, redirect
from gym.models import Contact, Chats
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.


def index(request):
    if request.method == "POST":
        message = request.POST['msg']
        mess = Chats(quries=message)
        mess.save()
        messages.success(request, "We Will Reply You Soon")
        return redirect('home')
    else:
        return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def price(request):
    return render(request, 'price.html')


@login_required(redirect_field_name='loginuser', login_url='/login')
def checkout(request):
    return render(request, 'checkout.html')


def signup(request):
    if request.method == "POST":
        # Get The Post Parameter
        username = request.POST['uname']
        first_name = request.POST['fname']
        last_name = request.POST['lname']
        email_id = request.POST['email']
        pass1 = request.POST['pass1']
        cpass2 = request.POST['pass2']

        # Checks For Error
        if len(username) > 10:
            messages.error(request, 'User Name Must Be Under 10 Character')
            return redirect('signup')

        if not username.isalnum():
            messages.error(
                request, 'Username must only Contain AlphaNumeric Value')
            return redirect('signup')

        if len(pass1) < 5:
            messages.error(request, 'Passward is Too Short')
            messages.error(request, 'Passward must be Greater Then 8 figure')
            return redirect('signup')

        if pass1 != cpass2:
            messages.error(request, 'Passward You Enter Does not match')
            return redirect('signup')
        # Creating The User
        myuser = User.objects.create_user(username, email_id, pass1)
        myuser.first_name = first_name
        myuser.last_name = last_name
        myuser.save()
        messages.success(
            request, 'Your Account Has been Created Sucessfully Now Please Login To Purchase Offer Of Gym')
        return redirect('login')

    else:
        return render(request, 'signup.html')


def loginuser(request):
    if request.user.is_authenticated:
        return redirect('home')

    else:

        if request.method == "POST":

            loginusername = request.POST['loginusername']
            loginpassword = request.POST['loginpassward']

            user = authenticate(username=loginusername, password=loginpassword)

            if user is not None:
                login(request, user)
                messages.success(
                    request, "You Have Login Successfully Now You Can Checkout")
                return redirect('home')
            else:
                messages.error(
                    request, "Invalid Credentials || Please Try Again")
                messages.error(
                    request, "Details Doest not Match... Please Signup If Not Done")
                return redirect('login')

    return render(request, 'login.html')


@login_required(redirect_field_name='loginuser', login_url='/login')
def logoutuser(request):
    logout(request)
    messages.warning(request, "You Have Successfully Logout From Account")
    return redirect('home')


@login_required(redirect_field_name='loginuser', login_url='/login')
def contact(request):
    if request.method == "POST":

        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        mobile = request.POST['mobile']
        desc = request.POST['desc']

        if len(fname) < 2:
            messages.error(request, 'Please Fill The First Name Correctly')
        elif len(email) < 5:
            messages.error(request, 'Please Fill Email Correctly')
        elif len(lname) < 2:
            messages.error(request, 'Please Fill Last Name Corerectly')
        elif len(mobile) < 8:
            messages.error(request, 'Please Fill Mobile Name Correctly')
        elif len(desc) < 10:
            messages.error(request, 'Plz Fill The Description Correctly')
        else:
            contact = Contact(first_name=fname, last_name=lname,
                              email_id=email, mobile_no=mobile, description=desc)
            contact.save()
            messages.success(request, 'Your Form Is Submitted Successfully.')
            messages.success(request, 'We Will Contact You Shotly.')
    return render(request, 'contact.html')
