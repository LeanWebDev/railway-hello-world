from django.http import HttpResponse


def index(request):
    return HttpResponse("Choo Choo! This is your Django app 🚅. We just tested a change.")
