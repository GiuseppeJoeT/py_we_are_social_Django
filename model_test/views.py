from django.shortcuts import render
from model_test.models import Contact


def get_contacts(request):
    return render(request, "model-Test/home.html",
                  {'contact_list': Contact.objects.all()})
