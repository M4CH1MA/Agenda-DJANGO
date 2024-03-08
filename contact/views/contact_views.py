from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from contact.models import Contact
from django.core.paginator import Paginator


# Create your views here.
def index(request):
    contacts = Contact.objects.filter(show=True).order_by('-id')

    paginator = Paginator(contacts, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    #print(contacts.query) #mostra a query

    context = {
        'page_obj': page_obj,
        'site_title': 'Contatos - '
    }

    return render(
        request,
        'contact/index.html',
        context
    )

def search(request):
    search_value = request.GET.get('q', '').strip() #pegar o que esta dentro do q (url)
    
    if search_value == '':
        return redirect('contact:index')

    contacts = Contact.objects.filter(show=True).filter(Q(first_name__icontains=search_value) | Q(last_name__icontains=search_value)).order_by('-id')

    paginator = Paginator(contacts, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    #print(contacts.query) #mostra a query

    context = {
        'page_obj': page_obj,
        'site_title': 'Contatos - ',
        'search_value': search_value,
    }

    return render(
        request,
        'contact/index.html',
        context
    )

def contact(request, contact_id):
    #single_contact = Contact.objects.filter(pk=contact_id).first()
    single_contact = get_object_or_404(Contact, pk=contact_id, show=True)
    
    site_contato = f'{single_contact.first_name} - '

    context = {
        'contact': single_contact,
        'site_title': site_contato
    }

    return render(
        request,
        'contact/contact.html',
        context
    )