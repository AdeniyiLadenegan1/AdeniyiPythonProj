from django.shortcuts import render
from .forms import EnrolForm

from .models import account



from django.core import serializers
import json








# Create your views here.
def index(request):
    return render(request, 'skydzygn/index.html')

# def about(request):
#     return render(request, 'skydzygn/about.html')

def contact(request):
    return render(request, 'skydzygn/contact.html')

def portfolio(request):
    return render(request, 'skydzygn/portfolio.html')

def team(request):
    return render(request, 'skydzygn/team.html')





def about(request):
    if request.method == 'POST':
        submitted_form = EnrolForm(request.POST)
        if submitted_form.is_valid():
            
            # create variables for fname, lname, email.
            fname = submitted_form.cleaned_data['fname']
            lname = submitted_form.cleaned_data['lname']
            email = submitted_form.cleaned_data['email']
            address = submitted_form.cleaned_data['home address']
            phone = submitted_form.cleaned_data['phone number']
            bdate = submitted_form.cleaned_data['Date Of Birth']
            course = submitted_form.cleaned_data['chosen course']
            specialization = submitted_form.cleaned_data['specialization']
            password = submitted_form.cleaned_data['password']


            account_data_base = account.object.filter(Email=email)
            account_data_base = serializers.serialize('json', account_data_base)


            account_data = account(firstName = fname, lastName = lname, 
            Email =email, Address =address, Phone= phone, BirthDate =bdate, 
            Course = course, Specialization =specialization, Password = password)
            account_data.save()
            note = "Thank you for taking the time to enrol, Your success journey starts here"

            form = EnrolForm()
            return render(request, 'about.html', {'EnrolForm': form, 'note':note})

    else:
        form = EnrolForm()
        return render(request, 'about.html', {'EnrolForm': form})





# def about(request):
#     if request.method == 'POST':
#         submitted_form = aboutForm(request.POST)
#         if submitted_form.is_valid():
#             fname = submitted_form.cleaned_data['fname']
#             lname = submitted_form.cleaned_data['lname']
#             email = submitted_form.cleaned_data['email']
#             phone = submitted_form.cleaned_data['phone']
#             address = submitted_form.cleaned_data['address']
#             dateofbirth = submitted_form.cleaned_data['dateofbirth']
#             course = submitted_form.cleaned_data['course']
#             specialization = submitted_form.cleaned_data['specialization']
#             password = submitted_form.cleaned_data['password']


#             about_data = about(FirstName = fname, lastName = lname, Email =email, 
#             Address = address, DOB = dateofbirth, Course = course, Specialization =specialization, Phone = phone, Password = password)
#             about_data.save()
#             note = "You have enrolled successfully"       

#             form = aboutForm()
#             return render(request, 'about.html', {'aboutForm': form, 'note':note})

#     else:
#         form = aboutForm()
#         return render(request, 'about.html', {'aboutForm': form})

