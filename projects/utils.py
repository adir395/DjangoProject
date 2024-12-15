from .models import Project, Tag
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage



def searchProject(request):
    search = ''
    if request.GET.get('search_query'):
        search = request.GET.get('search_query')
    tag = Tag.objects.filter(name__iexact=search)
    projects = Project.objects.distinct().filter(Q(title__icontains=search) | Q(owner__name__icontains=search) | Q(tags__in=tag))
    return projects, search


def paginateProjects(request, projects, results):

    page = request.GET.get('page')
    paginator = Paginator(projects, results)

    try:
        projects = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        projects = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        projects = paginator.page(page)

    leftIndex = (int(page) - 4)

    if leftIndex < 1:
        leftIndex = 1

    rightIndex = (int(page) + 5)

    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages + 1

    custom_range = range(leftIndex, rightIndex)

    return custom_range, projects