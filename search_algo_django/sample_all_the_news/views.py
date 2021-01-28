from django.shortcuts import get_object_or_404, render
import csv
from .models import AllTheNews
from .utils import import_data_from_csv
import time
from django.core.paginator import Paginator


def all_the_news_dataset(request):
    context = {}
    dataset = AllTheNews.objects.all()
    context.update({'search_summary': f'Showing all {len(dataset)} entries.'})

    if 'search' in request.GET:
        start = time.time()
        search_term = request.GET['search']
        dataset = AllTheNews.search(search_term)
        end = time.time()
        context.update({'search_summary': f'Filtered to {len(dataset)} entries in {round(end-start, 3)} seconds.'})

    paginator = Paginator(dataset, 25) 

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context.update({'page_obj': page_obj})
    return render(request, 'sample_all_the_news/all_the_news_dataset.html', context)

def all_the_news_detail(request, pk):
    object = get_object_or_404(AllTheNews, pk=pk)

    context = {'object': object}
    return render(request, 'sample_all_the_news/all_the_news_detail.html', context)