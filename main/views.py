

from django.shortcuts import render, redirect
from .forms import PersonForm



def mainview(request):
    return render(request, 'pages/main.html')

def aboutus(request):
    return render(request, 'pages/aboutus.html')

def services(request):
    return render(request, 'pages/services.html')



from django.shortcuts import render, redirect
from .forms import PersonForm

def contactus(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('coming_soon')
    else:
        form = PersonForm()

    return render(request, 'pages/contactus.html', {'form': form})

def coming_soon(request):
    return render(request, 'pages/coming_soon.html')

