
from app import repository
from app.forms import FormCreator

def get_headers(data):
    headers = repository.get_headers(data)
    return headers

def get_records(data):
    records = repository.get_records(data)
    return records

def exist_model(data):
    return repository.exist_model(data)
    
def create_form(data):
    headers = get_headers(data)
    types = repository.get_types(data)
    pointers = repository.get_pointers(data)
    options = []
    for i in range(len(types)):
        if types[i] == 'Select':
            pks = repository.get_all_pk(data)
            options.append(pks)
        elif types[i] == 'Choices':
            options.append(pointers[i])
        else:
            options.append('')
    form = FormCreator(data,headers,types,options)
    return form
