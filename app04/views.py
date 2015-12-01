from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import logout
from django.conf import settings
from app04.forms import StructureForm
from app04.models import StructureModel

# Create your views here.

##################
# NanoCore views # 
##################

def app04_view_nanocore_junction(request):
    context = {}
    return render(request, 'nanocore_junction.html', context)


def app04_view_nanocore_analysis(request):
    context = {}
    return render(request, 'nanocore_analysis.html', context)


from django.contrib.auth.decorators import login_required

@login_required
def app04_view_nanocore(request):
    context = {'filename':'',}

    # login required
    if not request.user.is_authenticated():
        return redirect(settings.LOGIN_URL)

    if request.method == "GET":
        edit_form = StructureForm()

    elif request.method == "POST":
        edit_form = StructureForm(request.POST, request.FILES)

        if edit_form.is_valid():
            saved = edit_form.save(commit=False)
            saved.user = request.user
            saved.save()

            # filename & path
            import os
            abspath  = os.getcwd()
            filename = request.FILES['structure']
            filepath = '/uploaded_files/structure_files/user_%s/%s+00:00/' % \
            (request.user.id, request.POST['created'])
            filepath_1 = filepath.split()[0]
            filepath_2 = filepath.split()[1]
            filepath = filepath_1 + '_' + filepath_2
            jsmolpath = filepath + str(filename)
            fullpath = abspath + filepath + str(filename)
            print fullpath

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
    temp = StructureModel.objects.all()
    results2 = []
    i = 1
    for t in temp:
        structure = str(t.structure).split('/')[-1]
        url = t.structure.url
        description = str(t.description)
        commands = str(t.commands)
        #i, user, struct, descript, comm, link
        print [i, structure, description, commands, url]
        results2.append([i, structure, description, commands, url])
        i += 1
    results2.reverse()

    # update context
    context['results2'] = results2
    context['form'] = edit_form
    return render(request, 'nanocore_viewer.html', context)


def app04_view_nanocore_view(request):
    context = {}
    return render(request, 'nanocore_view.html', context)
