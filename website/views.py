from django.shortcuts import render


def index(request):
    return render(request, "base.html")

def wochenplan(request):
    return render(request, "wochenplan.html")
