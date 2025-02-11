# Introduction

Al Hosn App is the official app of UAE to track the health status related to Covid-19. We have created a similar program that delivers the main features of the official Al Hosn App using Python and Python GUI for the showing the output. There are 2 ways a person can access the app, as a user or an admin. 

The user can view all his/her PCR and vaccination details. The user is required to enter his/her emirates ID number. Once the Emirates ID is found to be registered in the app, OTP is sent to the user’s email and then the user can view all the details.

The admins are required to enter their admin login and admin password to be granted access. The admin can view all the details of the users. They also perform important tasks like viewing all the positive cases, sending reminder emails to users who have not received their booster dose, keeping track of the total number of people choosing each vaccine (Sinopharm, Pfizer and Covaxin) and many more.

# Content

The main features include displaying the personal information of citizens such as  Name, Passport Number, Emirates Id, and Date of Birth. Other features that are related to the health status are displaying the number of days passed since the results of the last PCR test came, displaying the health pass which is green, gray, or red, it also displays the list of vaccination information the citizens have taken and finally displays the list of PCR Tests information. The green pass is obtained when the citizen has taken the vaccination dose within the time interval of 6 months from the previous vaccination dose and also has 30 days of a negative result of the PCR Test. The health pass is grey if the negative PCR result has passed 30 days time frame and also if the time frame of the last vaccination dose has passed 6 months. The health pass is red if the latest PCR Test has positive results.

The input data includes the 3 text files which are Person_info, PCR_Info, and Vaccination_Info. Person_Info file includes Names, Passport Number, Emirates ID, Email address, Date of birth, Emirate, and Age of registered UAE citizens. PCR_Info file includes Emirates ID, Test number, Test Result, and Date of PCR Test.  Vaccination_Info file includes Emirates ID, Doses, Vaccination name, and Date of Vaccination.

# Output

![image](https://github.com/user-attachments/assets/cece1e76-2799-4a49-8821-a9c71d61c0d5)

### As Admin:

![image](https://github.com/user-attachments/assets/3e643f1c-3a20-4a81-bed8-9f73dee20559)<br/>
![image](https://github.com/user-attachments/assets/d765ba27-69ad-4e30-86ca-4c5ea2580431)<br/>
![image](https://github.com/user-attachments/assets/374018b5-b423-4543-828c-3ea52f0f5015)

### As User:

![image](https://github.com/user-attachments/assets/6e720a2a-a316-4581-9be7-4bf49501eefa)<br/>
![image](https://github.com/user-attachments/assets/7382177f-5d7e-42a3-af72-e655315f74b7)<br/>
![image](https://github.com/user-attachments/assets/7c0b436f-eeb0-4056-a79a-18a1d771d405)











