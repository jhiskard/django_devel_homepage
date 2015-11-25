from django.shortcuts import render
from app02.forms import PublicationForm
from app02.models import Publication, Member
#from app02.models import SORT_OF_STATUS, SORT_OF_DEGREE, SORT_OF_ENDING

# Create your views here.

from django.http.response import HttpResponse
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def app02_view_publications(request):

    temp = Publication.objects.all().order_by('year', 'published_month', 'published_date')
    temp = temp.reverse()

    temp = Paginator(temp, 10)
    page = request.GET.get('page')

    try:
        posts = temp.page(page)
    except PageNotAnInteger:
        posts = temp.page(1)
    except EmptyPage:
        posts = temp.page(temp.num_pages)

    # initial data
    i = 1
    results = []
    for t in posts:
        try:
            thumbnail = t.thumbnail.url
        except:
            thumbnail = ''
        title = t.title
        authors = t.authors
        year =  t.year
        vol  =  t.vol
        issue = t.issue
        pages = t.pages
        doi =   t.doi
        link =  t.link
        abstract = t.abstract
        pub_m = t.published_month
        pub_d = t.published_date 

        results.append( [i, thumbnail, title, authors, year, 
                         vol, pages, doi, link, abstract, pub_m, pub_d] )
        i += 1

    context = {'posts': posts,
               'results'   : results, }
    return render(request, 'publications.html', context)


def app02_view_publications_index(request):
    context = {}

    if request.method == "GET":
        edit_form = PublicationForm()

    elif request.method == "POST":
        edit_form = PublicationForm(request.POST, request.FILES)

        if edit_form.is_vaild():
            saved = edit_form.save()

    context['form'] = edit_form
    temp = Publication.objects.all()

    i_break = 3
    i = 1
    results = []
    for t in temp:
        try:
            thumbnail = t.thumbnail.url
        except:
            thumbnail = ''
        title = t.title
        authors = t.authors
        year =  t.year
        vol  =  t.vol
        issue = t.issue
        pages = t.pages
        doi =   t.doi
        link =  t.link
        abstract = t.abstract
        pub_m = t.published_month
        pub_d = t.published_date 

        results.append( [i, thumbnail, title, authors, year, 
                         vol, pages, doi, link, abstract, pub_m, pub_d] )
        i += 1

    # sort data
    results.sort(key=lambda l: (l[4], l[10], l[11]), reverse=True)

    results = results[:i_break]
    context['results'] = results
    return render(request, 'index.html', context)


from django.contrib.auth.decorators import login_required

@login_required

def app02_view_people_member(request):

    # login required
    if not request.user.is_authenticated():
        return redirect(settings.LOGIN_URL)

    temp = Member.objects.all().order_by('priority')

    # initial data
    results = []

    for t in temp:

        # for current members
        priority  = t.priority
        try:
            thumbnail = t.thumbnail.url
        except:
            thumbnail = ''
        name   = t.name
        status = t.status
        degree = t.degree
        fields = t.fields
        office = t.office
        email  = t.email 
        tel    = t.tel   
 
        # for graduate members
        is_graduate     = t.is_graduate
        end_as          = t.end_as          
        currentposition = t.currentposition 

        if not is_graduate:
            results.append( [priority, thumbnail, name, status, degree, 
                             fields, office, email, tel, is_graduate,
                             end_as, currentposition] )

    context = {'results': results, }

    return render(request, 'people_member.html', context)


def app02_view_people_prof(request):
    context = {}
    return render(request, 'people_prof.html', context)


def app02_view_people_alumni(request):

    # login required
    if not request.user.is_authenticated():
        return redirect(settings.LOGIN_URL)

    temp = Member.objects.all().order_by('priority')

    # initial data
    results = []

    for t in temp:

        # for current members
        priority  = t.priority
        try:
            thumbnail = t.thumbnail.url
        except:
            thumbnail = ''
        name   = t.name
        status = t.status
        degree = t.degree
        fields = t.fields
        office = t.office
        email  = t.email
        tel    = t.tel

        # for graduate members
        is_graduate     = t.is_graduate
        end_as          = t.end_as
        currentposition = t.currentposition

        if is_graduate:
            results.append( [priority, thumbnail, name, status, degree,
                             fields, office, email, tel, is_graduate,
                             end_as, currentposition] )

    context = {'results': results, }

    return render(request, 'people_alumni.html', context)


def app02_view_people_collab(request):
    context = {}
    return render(request, 'people_collab.html', context)
