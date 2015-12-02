from django.shortcuts import render, redirect
from django.conf import settings

# Create your views here.
from app03.forms import BoardModelForm
from app03.models import BoardModel
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

#
# Basic views
#

from django.contrib.auth.decorators import login_required

@login_required
def app03_view_board(request):

    # login required
    if not request.user.is_authenticated():
        return redirect(settings.LOGIN_URL)

    edit_form = BoardModelForm()

    temp = BoardModel.objects.all()
    temp.reverse()
    temp = Paginator(temp, 10)
    page = request.GET.get('page')

    try:
        posts = temp.page(page)
    except PageNotAnInteger:
        posts = temp.page(1)
    except EmptyPage:
        posts = temp.page(temp.num_pages)

    i = 1
    results = []
    for t in posts:
        id = t.id
        user = t.user
        title = t.title
        contents = t.contents
        created = t.created
        modified = t.modified
        results.append( [id, i%2, user, title, contents, created, modified] )
        i += 1

    context = {
               'results': results,
               'posts'  : posts,
              }

    return render(request, 'board.html', context)
