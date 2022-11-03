from django.shortcuts import render
# from django.http import HttpResponse
# from django.template import loader

from .models import Contact

# Create your views here.
def index(request):
  contacts = Contact.objects.all()
  # template = loader.get_template('contacts/index.html')
  context = {'contacts': contacts}
  return render(request, 'contacts/index.html', context)

def show(request, contact_id):
  contact = Contact.objects.get(pk=contact_id)
  context = {'contact': contact}
  return render(request, 'contacts/show.html', context)