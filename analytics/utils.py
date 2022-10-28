from collections import Counter

def process_authors(x):
    for author in x:
        keys_to_delete = []
        for key in author:
            if key != '_id' and key != 'name':
                keys_to_delete.append(key)
        for key in keys_to_delete:
            del author[key]
    return x


def add_citations_to_authors(row):
    for author in row['authors']:
        author['n_citation'] = row['n_citation']
    return row['authors']

def process_n_citations(x):
    c = Counter()
    for author in x:
        if 'name' in author.keys():
            c[author['name']] += 1
    return c