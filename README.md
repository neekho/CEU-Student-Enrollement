<a name="readme-top"></a>



<h1 align="center">Student Management</h1>

An unofficial Django rest framework Student Management System for Centro Escolar University Makati.

_____________________________________________________________________________________________________

<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]](https://example.com)


This is for performing CRUD operations in relation to managing students in a given organization. Currently the main focus of the project is to build a RESTful API with JWT. Addition of front-end will began soon, along with the integration of all API functions.

Features:
* Helpful error messages when a bad request happens.
* Scaleable to a complete system
* Uses JWT in making requests to the backend




<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With



* [![Python][Python.org]][Python-url]
* [![Django Restframework][Django-rest-framework.org]][Drf-url]
* [![SQLite][Sqlite.org]][Sqlite-url]
<!--* [![Bootstrap][Bootstrap.com]][Bootstrap-url] -->
<!--* [![JQuery][JQuery.com]][JQuery-url] -->

<p align="right">(<a href="#readme-top">back to top</a>)</p>




<!-- GETTING STARTED -->
## Getting Started

Download all the prerequisites below in order.

### Prerequisites
Download all of these to get started

* [Python](https://www/python.org)
* [Django](https://www.djangoproject.com)
* [Django Restframework](https://www.django-rest-framework.org)
* [Simple JWT](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/) 

### Installation

_Once installed, open a command prompt, choose your directory wherein you want to save the project. Finally, clone the repo._


1. Clone the repo
   ```sh
   C:\Users\PC> git clone https://github.com/neekho/CEU-Student-Enrollement.git
   ```
2. Go to the project folder
   ```sh
   C:\Users\PC> cd ceu
   ```
3. Create a superuser _Provide the neccessary information when prompt._
   ```sh
   C:\Users\PC\ceu> python manage.py createsuperuser
   ```
   
4. Run the local server either specify a port number or use the default (8000)
   ```sh
    C:\Users\PC\ceu> python manage.py runserver <OPTIONAL: PORTNUMBER>
   ```

_Once the local surver is running, open up a browser and go to http://localhost:8000/overview._


<p align="right">(<a href="#readme-top">back to top</a>)</p>

___________________________________________________________________________________________________

### Application Routes

1 Function based views API Routes
Refer here for all the list of available routes in the API. You may use Postman in testing the endpoints or the built-in browseable API.
Keep in mind, this is for all the function based view endpoints.

* [All Routes](http://localhost:8000/api/overview) _Returns all possible routess in JSON format_
* [Student List](http://localhost:8000/api/students)  _See all existing students in the database._
* [Single Object Student](http://localhost:8000/api/<id>) _Provide a student id at the end of this url or else this will result in a 404._
* [Create Student](http://localhost:8000/api/add)  _Create a student that will be save in the SQLite database._
* [Update Student](http://localhost:8000/api/update<id>)  _Update existing student data. Provide a student id at the end of this url._
* [Delete Student](http://localhost:8000/api/delete<id>)  _Delete an existing student. Provide a student id at the end of this url._


2 Class based views API Routes
 You may use Postman in testing the endpoints or the built-in browseable API. Do not forget to change the HTTP method to your desire outcome.

* [All Students or Create a Student](http://localhost:8000/api/cbv/students) _For returning all students, and adding a student. Only signed users can add a student with this route._
* [Single Object Student Update, and Delete](http://localhost:8000/api/cbv<id>) _For returning the matching student with the provided id num, updating it, or deleting that student. Provide a student id at the end of this url or else this will result in a 404._



3 Front-end Routes
Refer here for all the list of available routes in the application
* [Home](http://localhost:8000/home) _You will abe asked to login first before you can access the home page. Make you sure already created a super user account_
* [Login](http://localhost:8000/login)
* [Logout](http://localhost:8000/logout)














<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[product-screenshot]: images/screenshot.png

[Python.org]: https://img.shields.io/badge/Python-35495E?style=for-the-badge&logo=python&logoColor=white
[Python-url]: https://python.org/

[Django-rest-framework.org]: https://img.shields.io/badge/DjangoRestframework-33415E?style=for-the-badge&logo=python&logoColor=white
[Drf-url]: https://www.django-rest-framework.org


[Sqlite.org]: https://img.shields.io/badge/SQLite-6d93d1?style=for-the-badge&logo=SQLite&logoColor=white
[Sqlite-url]: https://www.sqlite.org/index.html


[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com 
