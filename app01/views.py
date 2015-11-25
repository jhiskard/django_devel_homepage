from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import logout


# Create your views here.
from app01.forms import UploadStructureForm
from app01.models import app01_UploadStructureModel

#
# Basic views
#

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


#
# NanoCore views
#

def app01_view_nanocore_junction(request):
    context = {}
    return render(request, 'nanocore_junction.html', context)


def app01_view_nanocore_analysis(request):
    context = {}
    return render(request, 'nanocore_analysis.html', context)


from django.contrib.auth.decorators import login_required

@login_required

def app01_view_nanocore(request):
    context = {'filename':'',}

    # login required
    if not request.user.is_authenticated():
        return redirect(settings.LOGIN_URL)

    if request.method == "GET":
        edit_form = UploadStructureForm()

    elif request.method == "POST":
        edit_form = UploadStructureForm(request.POST, request.FILES)

        if edit_form.is_valid():
            saved = edit_form.save(commit=False)
            saved.user = request.user
            saved.save()

            # filename & path
            import os
            abspath  = os.getcwd()
            filename = request.FILES['structurefile']
            filepath = '/uploaded_files/user_%s/%s+00:00/' % \
            (request.user.id, request.POST['created'])
            filepath_1 = filepath.split()[0]
            filepath_2 = filepath.split()[1]
            filepath = filepath_1 + '_' + filepath_2
            jsmolpath = filepath + str(filename)
            fullpath = abspath + filepath + str(filename)

            # NanoCore part
            import NanoCore as nc
            atoms = []

            if '.xsf' in str(filename):
                command_read = "atoms = nc.io.read_xsf('%s')" % fullpath
                exec command_read
                commands = request.POST['commands']
                exec commands
                command_write = "nc.io.write_xsf('%s', atoms)" % fullpath
                exec command_write

            elif '.xyz' in str(filename):
                command_read = "atoms = nc.io.read_xyz('%s')" % fullpath
                exec command_read
                commands = request.POST['commands']
                exec commands
                command_write = "nc.io.write_xyz('%s', atoms)" % fullpath
                exec command_write

            results = []
            i = 1
            for atm in atoms:
                symb = atm.get_symbol()
                x,y,z = atm.get_position()
                results.append([i, symb, x,y,z])
                i += 1

            context = {
                       'filename':  filename,
                       'jsmolpath': jsmolpath,
                       'results':   results,
                      }

    # accumulated data part
    temp = app01_UploadStructureModel.objects.all()
    results2 = []
    i = 1
    for t in temp:
        user = t.user
        structurefile = str(t.structurefile).split('/')[-1]
        description = str(t.description)
        commands = str(t.commands)
        if str(t.user) == str(request.user):
            results2.append([i, user, structurefile, description, commands])
        i += 1
        results2.reverse()

    # update context
    context['results2'] = results2
    context['form'] = edit_form
    return render(request, 'nanocore_viewer.html', context)


#
# Sign in/up views
#

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
