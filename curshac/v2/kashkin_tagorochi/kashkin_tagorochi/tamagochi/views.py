from django.shortcuts import render

def tamagochi(request):
    return render(request, 'index.html')

def plants(request):
    return render(request, 'plants.html')

def trash(request):
    return render(request, 'trash.html')