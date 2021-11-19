### This is the library management system. Its a website to register book records from the users and Admin can access user data by using CRUD API's. I used ViewSet classes to perform API funcations. I created register, login and logout page for user and admin as well. I used HTML,CSS,BOOTSTRAP in frontend. 

#### The Admin protal username is "superuser" and password is "superuser"

#### I would like to inform you if user wants to perfrom CRUD API funcations user needs to register via SIGNUP page. Once user will get register then superuser needs to enable the user's staff status. if user's staff status is green then user can access the api. I have used IsAdminUser permissions class so it is required that user's staff status should be green else it will show you an error for eg: 
![Inkedstaff_LI](https://user-images.githubusercontent.com/81191373/142484577-578c2cb7-5424-4188-9d71-0ac7899b9053.jpg)

#### Once your staff status is green then you can access the CRUD API funcations. you need to login via "For Administration" tab from the navbar. Afetr login you need to tap on below buttor "click here if you are an admin" 
![InkedInkedadmin_LI](https://user-images.githubusercontent.com/81191373/142486102-dfc3939f-be89-4a52-8b29-7d130f82fad4.jpg)

#### you can access POST and GET funcations from a single page because I have used ViewSet class and if you want to use UPDATE and DELETE funcation you need to enter "id" pk after the link for eg: http://127.0.0.1:8000/api/BookEntryAPI/2/ 2 is the id now you will get PUT option and you can update the details in id 2 instance.
![Inkedpk_LI](https://user-images.githubusercontent.com/81191373/142487045-008abb4b-6831-4de9-85ef-c43b611e6481.jpg)

#### without using "id" you will get Post option and Complete list of data on the same page due to ViewSet class.
![api](https://user-images.githubusercontent.com/81191373/142488822-6f47f13b-f724-4f33-a230-a1cd5b961dba.png)


### Other documentation is mentioned with the code side by side.

