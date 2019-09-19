# InstaKnow

InstaKnow is an open-source mobile application that allows you to analyse the sentiments of public and private profiles based on their post captions. 

This repository is the backend/REST API for the application, where all requests from the application are received in the form of a JSON object. After the sentiment analysis is done, and the sentiments are evaluated, these results are sent in the form of JSON back to the application, where they are displayed.

The backend has been made in python, where the REST API is served as a Flask web-application. The web-application  can be hosted temporarily using ngrok or any other viable option.

The ML implementation is that of NLP (Natural Language Processing), where the captions are analysed using the ```Vader Sentiment Analysis``` library. Scores are received in the form of positive, negative, neutral and compound values, after which their mean is sent back to the front-end application where they are displayed.

Public profiles do not require any authentication although if you want to view the sentiments of a private profile, you must provide credentials for an account that can access that private profile (follows it) for authenticated access in order to extract the captions. 

## JSON

As mentioned above, this repo is a REST API that communicates using JSON objects.

**JavaScript Object Notation (JSON)** is an open-standard file format that uses human-readable text to transmit data objects consisting of attribute–value pairs and array data types (or any other serializable value). It is a very common data format, with a diverse range of applications. Such as serving as replacement for XML in AJAX systems.

An example:

```json
{
  "squadName": "Super hero squad",
  "homeTown": "Metro City",
  "formed": 2016,
  "secretBase": "Super tower",
  "active": true
}
```

## Data Format

The format in which data is transferred can be seen as follows:

### Application to Server :

* Public profile

```json
{
  "type":"Public",
  "login_id":"some_public_username"
}
```

* Private profile

```json
{
  "type":"Private",
  "login_id":"some_private_username",
  "login_username":"username_for_authentication",
  "password":"password_for_authentication"
}
```

### Server to Application:

* Success:

```json
{
  "type":"Success",
  "Value":result,
  "Picture":profile_picture_link,
  "Name":full_name_of_profile
}
```

* Fail:

```json
{
  "type":"Fail",
  "Value":error_message,
}
```

## Installation and Execution

Download or clone the repository in a directory and cd into folder containing the file ```app.py```.

* Set the FLASK environment variable FLASK_APP to the name of the python file as follows in the terminal (for Windows):

  
```python
set FLASK_APP=app.py 
```

* Run the flask app using the following command:

```python
flask run 
```

## Prospective Changes

* Adding encryption to ensure user security while analyzing private profiles

* Analysis based on comments of other followers on the user's posts
* Permanent deployment as a web-service on platforms like AWS instead of using ngrok.

* Checking policies and ensuring that publishing this application to the playstore/appstore should not cause instagram policy-violation due to web-scraping.


## License
[GPL 3.0](https://choosealicense.com/licenses/gpl-3.0/)