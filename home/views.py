from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from home.models import Setting, ContactFormu, ContactFormMessage
from hotel.models import Hotel, Category


def index(request):
    setting = Setting.objects.get
    sliderdata = Hotel.objects.all()[:4]
    category = Category.objects.all()  # kategory 'leri çağıralım
    context = {'setting': setting,
               'category': category,  # kategory 'leri index saygasına gönderiyoruz
               'page': 'home',
               'sliderdata': sliderdata}
    return render(request, 'index.html', context)



def hakkimizda(request):
    setting = Setting.objects.get
    category = Category.objects.all()  # kategory 'leri çağıralım
    context = {'setting': setting,
               'category': category,
               }
    return render(request, 'hakkimizda.html', context)


def iletisim(request):

    if request.method == 'POST':
        form = ContactFormu(request.POST)
        if form.is_valid():
            data = ContactFormMessage()
            data.name = form.cleaned_data['name']
            data.email = form.cleaned_data['email']
            data.subject = form.cleaned_data['subject']
            data.message = form.cleaned_data['message']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()  # veri tabanına kaydet
            messages.success(request, "Mesajınız basarı ile gönderilmiştir. Tesekkür ederiz.")
            return HttpResponseRedirect('/iletisim')

    setting = Setting.objects.get
    form = ContactFormu()
    category = Category.objects.all()  # kategory 'leri çağıralım
    context = {'setting': setting,
               'form': form,
               'category': category,
               }
    return render(request, 'iletisim.html', context)
