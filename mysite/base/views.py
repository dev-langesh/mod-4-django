from django.http import HttpResponse

def base(request):
    return HttpResponse("base!!!")