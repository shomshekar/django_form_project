from django.shortcuts import render
from . import forms

# Create your views here.
def form_name_view(request):
    form = forms.FormName()
    # Check to see if we are getting a POST request back
    if request.method == "POST":
        form = forms.FormName(request.POST)
        # Then we check to see if the form is valid
        if form.is_valid():
            print("Form validation successfull See console for information")
            print("Name : "+form.cleaned_data['name'])
            print("Email : "+form.cleaned_data['email'])
            print("Message : "+form.cleaned_data['text'])

    return render(request, "home.html", {'form':form})
