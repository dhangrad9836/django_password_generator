from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
#view for the home page
def home(request):
    return render(request, 'generator/home.html')
#view for the about page
def about(request):
    return render(request, 'generator/about.html')

def password(request):

    characters = list('abcdefghijklmnopqrstuvwxyz')

    #now add if/else if the user wants uppercase or checks uppercase
    if request.GET.get('uppercase'):
        #the extend method will add the uppercase list of characters to the lowercase list or what is inside
        #the .extend method ...which happens to be uppercase letters.
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()'))
    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))
    #so we have our length variable which we are assigning a request with GET and with that we
    #are going to get('length') the length comes from the home.html page where inside our form the select
    #has a 'length' assigned to it and the user will select the length of password with the dropdown arrow
    #also note that the number 12 is a default character in case the user does not select a number for how many
    #characters they want for the password.
    length = int(request.GET.get('length', 12))

    thepassword = ''
    for x in range(length):
        thepassword += random.choice(characters)


    #this will pass the variable thepassword to the url password.html
    return render(request, 'generator/password.html', {'password': thepassword})