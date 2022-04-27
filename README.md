# Equipement Management System

## Purpose of this project
* Develop a complete REST API with the connection using token authorization
* Write unit tests to test the source code

## Table of Content

* [Requirements](#requirements)
* [Schema](#schema)
* [API](#api)

## Local setup

1. Must have Python 3 installed and running
1. Clone the repo and cd into repo
1. Create a virtual environment: `python -m venv venv`
1. Go into your virtual environment: `venv/Script/activate`
1. Install dependencies: `pip install -r requirements.txt`
1. Create an admin user for logging into the Django admin interface: `python manage.py createsuperuser`
1. Run the app: `python manage.py runserver`
1. View the API at `localhost:8000` and the admin interface at `localhost:8000/admin`

## Requirements

* Develop REST API endpoints which are accessable to only authorized users
* For each endpoint, users can: list, create, retrieve, update, delete
  * list:
    * Return 1 list with classic pagination: related fields are returned in form of list of ID. For example for each equipment, the field "categories" is 1 list of ID
    * Pagination: Client API form: http://api.example.org/accounts/?page=4&page_size=100 . By default, if "page_size" is not defined as query parameters, the endpoint returns 30 elements and the number of maximum elements returned is 100.
    * Filters: should be structured as follows:
      * categories:
        * parent(simple)
      * equipements:
        * categories(multiple)
        * quantite (type "range" with "quantity_min" & "quantity_max")
  * Create
     * Each filed should be allowed to be written
   * Update
     * Each filed should be allowed to be updated
   * Update
     * Each filed should be allowed to be deleted
   * Retrieve
     * Return "detailed" children serializers. For example, the field "categories" is 1 object of details of this categories (name, slug, etc).

## Schema

* Categories
  * id
  * name(require, unique)
  * slug (require)
  * description
  * photo (simple)
  * parent (type tree, use Django MPTT model)

* Equipements
  * id
  * name
  * slug(require)
  * categories (multiple)
  * quantity

## API

**/categories/list/**

* get 
* post

**/categories/id**

* get
* put
* delete

**/equipements/list/**

* get
* post

**/equipements/id**

* get
* put
* delete

*example response:*

```json
{
  "id": 3,
    "categories": [
        {
            "id": 19,
            "name": "Electronics",
            "slug": "electronics",
            "description": "electronic devices",
            "photo": "/media/image/electronics.jpeg",
            "parent": null
        },
        {
            "id": 26,
            "name": "Smart TV",
            "slug": "smart-tv",
            "description": "smart devices",
            "photo": null,
            "parent": 19
        }
    ],
    "name": "SAMSUNG 50-Inch Class Neo QLED QN90A",
    "slug": "SAMSUNG-50-Inch-Class-Neo-QLED-QN90A",
    "quantity": 40
}
```
