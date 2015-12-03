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
            filepath = '/uploaded_files/structure_files/user_%s/%s_00_00/' % \
            (request.user.id, request.POST['created'].replace(':','_'))
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
        struct_id = t.id
        structure = str(t.structure).split('/')[-1]
        url = t.structure.url
        description = str(t.description)
        commands = str(t.commands)
        print [i, structure, description, commands, url]
        results2.append([struct_id, structure, description, commands, url])
        i += 1
    results2.reverse()

    # update context
    context['results2'] = results2
    context['form'] = edit_form
    return render(request, 'nanocore_viewer.html', context)


def app04_view_nanocore_view(request, struct_id):
    context = {}

    # login required
    if not request.user.is_authenticated():
        return redirect(settings.LOGIN_URL)

    edit_form = StructureForm()
    temp = StructureModel.objects.all()

    for t in temp:
        if int(t.id) == int(struct_id):
            print "matched:", t.id, struct_id
            structure = t.structure.url
            filename = structure.split('/')[-1]
            import os
            abspath = os.getcwd()
            fullpath = abspath + structure

            # NanoCore part
            import NanoCore as nc
            atoms = []
 
            if '.xsf' in str(filename):
                command_read = "atoms = nc.io.read_xsf('%s')" % fullpath
                exec command_read
 
            elif '.xyz' in str(filename):
                command_read = "atoms = nc.io.read_xyz('%s')" % fullpath
                exec command_read
 
            results = []
            i = 1
            for atm in atoms:
                symb = atm.get_symbol()
                x,y,z = atm.get_position()
                print i, symb, x,y,z
                results.append([i, symb, x,y,z])
                i += 1
            context = {'results': results,}

    return render(request, 'nanocore_view.html', context)


from xml.etree.ElementTree import parse
import os

def detail(request, xml_name):
    atrrib_list = []

    try:
        tree = parse("./uploaded_files/"+xml_name)
        note = tree.getroot()
        parameterList = note.find("{http://www.xml-cml.org/schema}parameterList")

        for child in parameterList:
            child_list = []

            if "name" in child.attrib:
                child_list.append(child.attrib["name"])

            else:
                child_list.append(child.attrib["title"])
                child_list.append(child.findtext("{http://www.xml-cml.org/schema}scalar"))
                atrrib_list.append(child_list)

    except IOError, e:
        atrrib_list = []

    context = {"atrrib_list": atrrib_list,}
    return render(request, "detail.html", context)
