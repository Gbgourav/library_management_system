# library_management_system
This is the library management system by using django. In this web site user can register his book record 
admin can get details of user which help admin to get books details record in his library...

#models.py here we can create book entry tables this is responsible to create table in our data base alsoit interects with serializer class

#In serializer class this will converting complex data such as querysets and modelto native phythin data types. that can easily rendered intiO JSON
#In bookEntry funcation. This will get the data from any user in front end This funcation is responsible to post data in our data set
#@Login_required decorater is used not to render any page via link ,if someone will write the link to get the derict access this will rederect user to the login page
#I usered post method to save data in our database. I usees messages to show if request get successful
#In This is the singup funcation class I created here I have used inbuilt signup class of django This func is responsible to save user data in our database 
#I usered the ViewSet class of django to create API funcations. django provide inbuilt ViewSet. We can improt this from the reset_framework. that does not provide any method like post() get() and many other that means it easy and time saving option to create api.
#In authentication_class I have used SessionAuthentication because this allows user
# to get inbuilt login and logout page while access the api and its more secure then BasicAuthentication


# In usered permission_class I have used IsAdminUser. This class will only allow those users whose 
# staff status is enabled of eg: if superuser enabled staff status of user then user can access the api's 
# otherwise user will getting an authentication error.

# home, about and index these are the basic func to render the html pages if 
# someone hit the url for eg: http://127.0.0.1:8000/home  then home funcation will 
# call and it will render user request to the index.html page 



# I create a class by using inbult SignUpForm class to register user. it looks like models class but django provide some builtin 
# features to create login page, logout page and change passwored features I took one the SignUpForm class 
# I added some additinol fields like passwored confirmation and email. I userd bootstrap form class "form-control" this class give a good UI to the user.  

# I used UserCreationForm, AuthenticationForm, UsernameField. These are the inbuilt features of django. UserCreationForm is used for creating a 
# new user that can use our web application.AuthenticationForm gives permissions: Binary (yes/no) flags designating whether a user may perform a certain task.
# if user is authentacated it will allow user. AuthenticationForm it define the forms fields.

# "Widget" representation of an HTML input element and "fiels" is used data types to store a particular type of data. For example, to store an integer, IntegerField




# I created LoginForm class to login user in our app this is also a builtin feature of the django. I usered "form-control" 
# bootstrap class to give good UI for user
# gettext, gettext_lazy as _ func provide software internationalization. as I appied _('Password') that means passwred lanugage 
# sould be based on setting.py language.

# I used Router for 'api/' to auto config the urls.Routers provides a simple, quick and consistent way of wiring ViewSet logic to a set of URLs. 
# views.SignUpFormView.as_view() is calling a static method on the SignUpFormView class, which constructs and returns an 
# instance of SignUpFormView if we see in views.py we have func SignUpFormView so if someone will hit the /signup then SignUpFormView will run.
# I used auth_views.LoginView.as_view to show the login form and perform the actions in it. Its a builtin funcation. We import LoginForm from froms.py to perform the actions.
# I used auth_views.LogoutView.as_view to get message if user is logout and user can rederct to the "login.html" if user is logout. its a builtin funcation.


