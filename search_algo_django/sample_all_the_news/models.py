from django.db import models
import csv
from search_algo.algo import SearchAlgoModel

class AllTheNews(SearchAlgoModel):
    title = models.CharField(max_length=256)
    publication = models.CharField(max_length=256)
    author = models.CharField(max_length=256)
    date = models.DateTimeField()
    year = models.IntegerField()
    month = models.IntegerField()
    url = models.CharField(max_length=1024)
    content = models.TextField()

    non_summarized_search_fields = ['title', 'publication', 'author']
    summarized_search_fields = ['content']
                    

