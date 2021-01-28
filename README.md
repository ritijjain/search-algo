# SearchAlgo
A lightweight python based text search for Django.

SearchAlgo uses nltk to clean data and gensim to pickup keywords from longer text fields. This infromation is stored in a `search_algo_condense` text field in the database allowing for speedy and accurate search results.

## Usage
* Add import `from search_algo_app.algo import SearchAlgoModel`
* Models using SearchAlgo should be a subclass of SearchAlgoModel
* Process search_algo_condense:
```shell
python manage.py shell
from <app_name>.models import <model> # Replace with your own app name and model name.
<model>.process_condense() # Usually takes less than 0.05 seconds per database entry.
```
* `<model>.search(<query>)` returns a QuerySet for the search

## Settings
All settings are defined as variables in the model.

| variable name | type | description | required | default |
| -- | -- | -- | --| -- |
| `non_summarized_search_fields` | list of strings | Shorter, more relevant model text fields which are stored in full in the `search_algo_condense` field used by the database for regular searches. | Yes | None |
| `summarized_search_fields` | list of strings | Longer model text fields which are processed for keywords to be stored in the `search_algo_condense` field. | No | None |
| `spell_check` | boolean | Defines if queries are checked and corrected for spelling. | No | False |

## Testing with Sample AllTheNews Dataset
Sample data compiled using [All the news dataset](https://www.kaggle.com/snapcrack/all-the-news) by Andrew Thompson.

* Download [sample dataset json file](https://mega.nz/file/smpgwS5Z#mVIeyQbqC8Sv4A2w5balkXtOfwCXG4QwX8zq-xqFiKc).
* Run `python manage.py loaddata <path to sample_all_the_news.json>`
* * Process search_algo_condense:
```shell
python manage.py shell
from <app_name>.models import <model> # Replace with your own app name and model name.
<model>.process_condense() # Usually takes less than 0.05 seconds per database entry.
```

## Screenshots
A specific search returns only few results.
![](/screenshots/specific_search.png)

A vague search would return a lot of results.
![](/screenshots/vague_search.png)

Exact searches using `--exact` can be used to fetch very specific entries.
![](/screenshots/exact_search.png)

Misspelled searches should work as expected with `spell_check = True`.
![](/screenshots/misspelled_search.png)

Misspelled searches with the `--exact` flag will usually result in 0 results.
![](/screenshots/exact_misspelled_search.png)