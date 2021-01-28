import csv
from .models import AllTheNews

def import_data_from_csv(csv_path, start_row, max_count):
    file = open(csv_path)
    csv_reader = csv.reader(file)
    next(csv_reader)

    max_count_counter = 0
    loop_count = 0

    for row in csv_reader:

        loop_count += 1
        if loop_count < start_row:
            continue

        obj = AllTheNews.objects.get_or_create(
            id = row[1],
            defaults={
                'title': row[2],
                'publication': row[3],
                'author': row[4],
                'date': row[5],
                'year': int(float(row[6])),
                'month': int(float(row[7])),
                'url': row[8],
                'content': row[9],
            }
            
        )

        if obj[1]:
            print(f'Added AllTheNews object with title {obj[0].title}')
        else:
            print(f'Updated AllTheNews object with title {obj[0].title}')

        max_count_counter += 1
        if max_count_counter >= max_count:
            break