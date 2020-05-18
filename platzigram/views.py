# Django
from django.http import HttpResponse
from django.http import JsonResponse

# Utilities
from datetime import datetime

def hello_world(request):
    now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    return HttpResponse(str(now))

def sort_integers(request):
    """Order a list of numbers"""
    # import pdb; pdb.set_trace()
    numbers = request.GET['numbers'].split(',')

    # Convert numbers from str to int
    numbers = list(map(lambda n: int(n), numbers))

    sorted_numbers = sorted(numbers)

    data = {
        'status': 'ok',
        'numbers': sorted_numbers,
        'message': 'integers sorted succesfully'
    }

    return JsonResponse(data, safe=False)

def say_hi(request, name, age):
    if age < 12:
        message = 'sorry {}, you are not allowed here'.format(name)
    else:
        message = 'Hello, {}! Welcome to Platzigram'.format(name)
    return HttpResponse(message)