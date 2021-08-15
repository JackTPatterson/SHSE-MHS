from django.shortcuts import get_object_or_404, redirect, render
from .forms import AnnouncementEditForm, FeedbackForm, AnnouncementForm, DatesForm, DatesEditForm
from .models import Dates, Feedback, Announcement
from django.contrib import messages
from django.contrib.auth import authenticate, login as dj_login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from random import randint
from django.views.generic.edit import DeleteView
from django.urls import reverse
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
# Create your views here.

def index(request):
    return render(request, "users/index.html")

def about(request):
    return render(request, "users/about.html")

def forms(request):
    return render(request, "users/forms.html")

def signup(request):
    return render(request, "users/signup.html")

def contact(request):
    context = {
        'feedbackAmt': Feedback.objects.all().count(),
    }
    return render(request, "users/contact.html", context)

def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)

    
def contactTechnical(request):
    form = FeedbackForm(request.POST)
    if request.method == "POST":
        ticket = random_with_N_digits(7)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.ticket = ticket
            obj.isTechnical = True
            form.save()

            subject, from_email, to = 'Thank You For Your Feedback', 'jpdigital@gmail.com', 'jtyler03@optonline.net'

            html_content = render_to_string('users/email.html', {'name': Feedback.objects.get(ticket=ticket).first_name, 'ticket': ticket}) # render with dynamic value
            text_content = strip_tags(html_content) # Strip the html tag. So people can see the pure text at least

            msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()


            messages.success(request, 'Thank you for submitting your feedback')
            return redirect('index')
    context = {
        'form': form
    }
    return render(request, "users/technical-contact.html", context)
    


def contactGeneral(request):

    form = FeedbackForm(request.POST)
    if request.method == "POST":
        ticket = random_with_N_digits(7)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.ticket = ticket
            obj.isTechnical = False
            form.save()

            subject, from_email, to = 'Thank You For Your Feedback', 'jpdigital@gmail.com', 'jtyler03@optonline.net'

            html_content = render_to_string('users/email.html', {'name': Feedback.objects.get(ticket=ticket).first_name, 'ticket': ticket}) # render with dynamic value
            text_content = strip_tags(html_content) # Strip the html tag. So people can see the pure text at least

            msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()


            messages.success(request, 'Thank you for submitting your feedback')
            return redirect('index')
    context = {
        'form': form
    }
    return render(request, "users/general-contact.html", context)

def login(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password =request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                dj_login(request, user)
                return redirect('announcements')
            else:
                messages.info(request, 'Username OR password is incorrect')

        context = {}
        return render(request, 'users/login.html', context)



class General(LoginRequiredMixin, ListView):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    model = Feedback
    template_name = 'users/feedback'  # ! This should not work but it does
    context_object_name = 'feedback'
    ordering = ['-date']

class Announcements(ListView):
    model = Announcement
    template_name = 'users/announcement'  # <app>/<model>_<viewtype>.html
    context_object_name = 'announcements'
    ordering = ['date']

class DatesList(ListView):
    model = Dates
    template_name = 'users/dates'  # <app>/<model>_<viewtype>.html
    context_object_name = 'dates'
    ordering = ['id']

def addDates(request):
    form = DatesForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            
            return redirect("/dates")
    context = {
        'form': form
    }
    return render(request, 'users/add-dates.html', context)

def addAnnouncements(request):
    form = AnnouncementForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            obj = form.save(commit = False)
            obj.announcementID = random_with_N_digits(7)
            form.save()
            return redirect("/announcements")
    context = {
        'form': form
    }
    return render(request, 'users/add-announcements.html', context)



def editAnnouncements(request, announcementID):
    instance = get_object_or_404(Announcement, announcementID=announcementID)
    
    form = AnnouncementEditForm(request.POST or None, instance=instance)
    if request.method == "POST":
            if form.is_valid():
                obj = form.save(commit = False)
                obj.announcementID = announcementID
                obj.save()
                return redirect('announcements')



    context = {
        'form': form,
        'instance': instance,
        
    }
    return render(request, 'users/announcements-edit.html', context)

def editDates(request, pk):
    instance = get_object_or_404(Dates, pk=pk)
    
    form = DatesEditForm(request.POST or None, instance=instance)
    if request.method == "POST":
            if form.is_valid():
                form.save()
                return redirect('/dates')
    context = {
        'form': form,
        
    }
    return render(request, 'users/dates-edit.html', context)
class deleteAnnouncements(DeleteView):

    template_name = 'users/announcement-delete.html'

    # specify the model you want to use
    def get_object(self):
        id_ = self.kwargs.get("announcementID")
        return get_object_or_404(Announcement, announcementID=id_)

    def get_success_url(self):
        return reverse('announcements')


class deleteDates(DeleteView):
    
    template_name = 'users/dates-delete.html'

    # specify the model you want to use
    def get_object(self):
        id_ = self.kwargs.get("pk")
        return get_object_or_404(Dates, pk=id_)

    def get_success_url(self):
        return reverse('dates')

