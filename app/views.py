from django.shortcuts import render
from django.contrib import messages
from app.forms import SignUpForm
# Create your views here.
def userForm(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            form = SignUpForm(label_suffix='')
    else:
        form = SignUpForm(label_suffix='')
    return render(request, 'app/index.html', {'form':form})

