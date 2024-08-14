**URL Shortener API Assignment**

**Overview**

The URL Shortener API allows users to shorten long URLs and retrieve the original URLs using
a short code. It is built using FastAPI and PostgreSQL. This documentation provides details on
how to set up, run, and use the API. Database is deployed in a liver server using render and
FastAPI application is deployed using vercel app, details are mentioned below.

**Features**

● Shorten URL: Accept a long URL and return a shortened version.
● Redirect to Original URL: Retrieve the original URL using the shortened code and
redirect to it.
● Retrieve All URL Details: Fetch all stored URLs and their corresponding short codes.

**Technology Stack**
● FastAPI: For building the web API.
● PostgreSQL: For storing the original URLs and their corresponding short codes.
● SQLAlchemy: For database ORM.
● Pydantic: For data validation and serialization.
● Render: For Database deployment
● Vercel: For Backend deployment

**Requirements**
● Python 3.8+
● PostgreSQL
● FastAPI
● SQLAlchemy
● Uvicorn (for running the FastAPI application)


**Live Application Details**

URL Shortener Application is deployed using Vercel. You can interact with the live application
and test the endpoints directly.
● Swagger UI: Access the API documentation and test endpoints at https://url-shortner-six-pi.vercel.app/docs . This interface allows you to explore and test the API
without needing to set up the project locally.
● Redirecting URL: To test URL redirection, use the localhost URL format with the short
code. For example, if you have a short code 356a1b, you can test redirection by visiting:
http://localhost:8000/redirect/356a1b
This will redirect you to the original URL associated with the short code.



**please refer to the documentation for more details**

**Documentation link** : https://docs.google.com/document/d/1BXGQyzuzvfXXcmdPLK75z7ai2GMI0wclMBd7u-atuyc/edit?usp=sharing
