from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm


def index(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Message submitted successfully.")
            return redirect("/#contact-form")
    form = ContactForm()
    context = {
        "form": form
    }
    return render(request, 'main_site/index.html', context=context)
