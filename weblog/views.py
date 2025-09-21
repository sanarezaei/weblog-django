from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Weblog, Tag

def search(request):
    if request.method == "POST":
        searched = request.POST['searched']
        weblogs_title = Weblog.objects.filter(title__contains=searched)

    return render(request, 'weblogs/search.html', {
        'searched': searched, 
        'weblogs_title': weblogs_title
    })

class WeblogListView(generic.ListView):
    model = Weblog
    paginate_by = 2
    template_name = 'weblogs/weblog_list.html'
    context_object_name = "weblogs"

class WeblogDetailView(LoginRequiredMixin, generic.DetailView):
    model = Weblog
    template_name = 'weblogs/weblog_detail.html'
    context_object_name = 'weblog'


def weblogs_by_tag(request, tag_id):
    tag = get_object_or_404(Tag, id=tag_id)
    weblogs = tag.weblogs_tag.all()

    return render(request, 'weblogs/weblogs_by_tag.html', {
        'tag': tag, 
        'weblogs': weblogs
    })

def weblog_list(request, tag_slug=None):
    object_list = Weblog.objects.all()
    paginator = Paginator(object_list, 4)
    page_number = request.GET.get('page')

    try:
        weblogs = paginator.page(page_number)
    except PageNotAnInteger:
        weblogs = paginator.page(1)
    except EmptyPage:
        weblogs = paginator.page(paginator.num_pages)

    return render(request, 'weblogs/pagination.html', {
        'page': weblogs, 
        'weblogs': weblogs
    })
