### The Admin protal username is "superuser" and password is "superuser"

### I would like to informed you if user want to perfrom CRUR API funcations user needs to register via login page. Once user will get register then superuser needs to enable the user's staff status. if user's staff status is green then user can access the api. I have used IsAdminUser permissions class so it is required that user's staff status should be green else it will show you an error for eg: 
![Inkedstaff_LI](https://user-images.githubusercontent.com/81191373/142484577-578c2cb7-5424-4188-9d71-0ac7899b9053.jpg)

### Once your staff status is gree then you can access the CRUR API funcations. you need to login via "For Administration" tab from the navbar. Afetr login you need to tap on below buttor "click here if you are an admin" 
![InkedInkedadmin_LI](https://user-images.githubusercontent.com/81191373/142486102-dfc3939f-be89-4a52-8b29-7d130f82fad4.jpg)

### you can access Create, Read, Delete funcations from a single page because I have used ViewSet calss and if you want to use PUT or Update funcation you need to enter "id" pk after the link for eg: http://127.0.0.1:8000/api/BookEntryAPI/2/ 2 is the id now you will get PUT option and you can update the details in id 2 instance.
![Inkedpk_LI](https://user-images.githubusercontent.com/81191373/142487045-008abb4b-6831-4de9-85ef-c43b611e6481.jpg)

### Other documentation is mentioned with the code side by side.

