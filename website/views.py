from django.shortcuts import render
from website.forms import ContactForm

def index_view(request):
    return render(request, 'website/index.html')

def about_view(request):
    return render(request, 'website/about.html')

def contact_view(request):
    if request.method == 'POST':
        modified_request = request.POST.copy()
        modified_request['name'] = 'Unknown'
        form = ContactForm(modified_request)
        if form.is_valid():
            form.save()
    form = ContactForm()
    return render(request, 'website/contact.html', {'form':form})
