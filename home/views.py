from django.shortcuts import render, redirect
from home.forms import SignUpForm
from django.contrib import messages
from datetime import datetime
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from home.models import BookEntry
from .serializers import BookEntrySerializer
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAdminUser
from rest_framework import viewsets
from django.contrib.auth.decorators import login_required




@login_required(login_url='/login/') 
def bookEntry(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        book = request.POST.get('book')
        author = request.POST.get('author')
        desc = request.POST.get('desc')
        create = BookEntry(name=name, book=book, author=author,desc=desc, date=datetime.today())
        create.save()
        messages.success(request, 'Your Message has been sent.')

    return render(request, 'bookEntry.html')

# This is the bookEntry funcation. This will get the data from any user in front end
# This funcation is responsible to post data in our data set

# @Login_required decorater is used not to render any page via link ,if someone will write the 
# link to get the derict access this will rederect user to the login page

# I usered post method to save data in our database. I usees messages to show if request get successful




class SignUpFormView(View):
    def get(self, request):
        form =  SignUpForm()
        return render(request, 'signup.html', {'form': form})
    def post(self, request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Congratuation!! Registered Successfully')
            form.save()
        return render(request, 'signup.html', {'form': form}) 
    
# This is the singup funcation class I created here I have used inbuilt signup class of django 
# This func is responsible to save user data in our database  





class BookEntryModelViewSet(viewsets.ModelViewSet):
    queryset = BookEntry.objects.all()
    serializer_class = BookEntrySerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAdminUser]
    
    
# I usered the ViewSet class of django to create API funcations. django provide inbuilt 
# ViewSet. We can improt this from the reset_framework. that does not provide any 
# method like post() get() and many other that means it easy and time saving option to create api.

# In authentication_class I have used SessionAuthentication because this allows user
# to get inbuilt login and logout page while access the api and its more secure then BasicAuthentication


# In usered permission_class I have used IsAdminUser. This class will only allow those users whose 
# staff status is enabled of eg: if superuser enabled staff status of user then user can access the api's 
# otherwise user will getting an authentication error.
    
    
    

def home(request):
     return render(request, 'index.html')
 
 
def about(request):
     return render(request, 'about.html')     
 
 

def index(request):
    return render(request, 'index.html') 



# home, about and index these are the basic func to render the html pages if 
# someone hit the url for eg: http://127.0.0.1:8000/home  then home funcation will 
# call and it will render user request to the index.html page 