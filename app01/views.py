from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import logout


# Create your views here.

############### 
# Basic views #
###############

def app01_view_index(request):
    context = {}
    return render(request, 'index.html', context)


def app01_view_publications(request):
    context = {}
    return render(request, 'publications.html', context)


def app01_view_research(request):
    context = {}
    return render(request, 'research.html', context)


def app01_view_contacts(request):
    context = {}
    return render(request, 'contacts.html', context)


def app01_view_schedule(request):
    context = {}
    return render(request, 'schedule.html', context)


####################
# Sign in/up views #
####################

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')


from django.core.urlresolvers import reverse
from app01.forms import SignupForm

def signup(request):
    """signup
    to register users
    """
    if request.method == "POST":
        signupform = SignupForm(request.POST)
        if signupform.is_valid():
            user = signupform.save(commit=False)
            user.email = signupform.cleaned_data['email']
            user.save()
            return HttpResponseRedirect(reverse("signup_ok"))

    elif request.method == "GET":
        signupform = SignupForm()

    return render(request, "signup.html", 
                  {"signupform": signupform,})

