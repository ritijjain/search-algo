from django.db import models
from django.db.models import Q
from gensim.summarization import keywords
import time
from textblob import TextBlob
from .utils import clean_str
import math


class SearchAlgoModel(models.Model):

    search_algo_condense = models.TextField(null=True)
    spell_check = False
    non_summarized_search_fields = None
    summarized_search_fields = None

    class Meta:
       abstract = True

    @classmethod
    def search(self, query):
        if '--exact' in query:
            query = self.process_search_string(query)
            return self.exact_search(query)
        
        processed_search_list = self.process_search_string(query)
        
        q_objects = Q()
        for item in processed_search_list:
            q_objects &= Q(search_algo_condense__icontains=item)

        return self.objects.filter(q_objects)

    @classmethod
    def exact_search(self, query):
        search_fields = self.non_summarized_search_fields + self.summarized_search_fields
      
        kwargs = {}
        for field in search_fields:
            kwargs.update({'{0}__{1}'.format(field, 'icontains'): query})
        
        q_objects = Q()
        for key, value in kwargs.items():
            q_objects.add(Q(**{key: value}), Q.OR)

        return self.objects.filter(q_objects)


    @classmethod
    def process_search_string(self, raw_query):
        if '--exact' in raw_query:
            cleaned_raw_query = raw_query.replace('--exact', '')
            return cleaned_raw_query

        cleaned_raw_query = clean_str(raw_query)

        if self.spell_check:
            cleaned_raw_query = self.process_spell_check(cleaned_raw_query)

        return cleaned_raw_query.split(' ')



    @classmethod
    def process_condense(self):
        
        model_set = self.objects.all()

        for object in model_set:
            start = time.time()
            condense_string = ''

            # Process summarized_search_fields.
            for field in self.summarized_search_fields:
                condense_string += str(getattr(object, field))

            object.search_algo_condense = keywords(condense_string, lemmatize=True).replace('\n', ' ')

            # Process non_summarized_search_fields.
            for field in self.non_summarized_search_fields:
                object.search_algo_condense += f' {clean_str(str(getattr(object, field)))}'
            object.save()
            end = time.time()

            print(f'Processed entry {object.pk} in {round(end-start, 3)} seconds')
        



    @classmethod
    def process_spell_check(self, string):
        text_blob = TextBlob(string)
        return text_blob.correct()