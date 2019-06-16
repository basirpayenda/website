from django.shortcuts import render, redirect
from django.core.mail import send_mail
from.forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Count
from blogs.models import Blog

def get_category_count():
    queryset = Blog \
        .objects \
        .values('category__title') \
        .annotate(Count('category__title'))
    return queryset


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data.get('subject')
            from_who = form.cleaned_data.get('email')
            message = form.cleaned_data.get('message')
            try:
                send_mail(subject, message, from_who, ['moi.basir@gmail.com'], fail_silently=False)
            except BadHeaderError:
                return HttpResponse('Bad header found')
            return redirect('contact:success')

    form = ContactForm()

    context = {
        'form':form, 
        'categories': get_category_count()
    }
    return render(request, 'contact/contact.html', context)


def success(request):
    return render(request, 'contact/success.html')


