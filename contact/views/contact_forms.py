from django.shortcuts import render
from contact.forms import ContactForm



# Create your views here.
def create(request):

    if request.method == 'POST':
        #print(request.POST.get("first_name"))
        context = {
            'form': ContactForm(request.POST)
        }

        return render(
            request,
            'contact/create.html',
            context
        )
    
    #method GET
    context = {
            'form': ContactForm()
        }

    return render(
        request,
        'contact/create.html',
        context
    )

    