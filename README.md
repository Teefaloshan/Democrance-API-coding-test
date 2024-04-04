# Democrance-API-coding-test
As I have descriped what I was trying to achieve but unfortunitly I had a couple of errors as the page is not found and to ty and fix this problem I have tried to create a new file "production_settings" and switch the DEBUG to false while in settings the DEBUG is true. I wish I had more time to try making this work, but I still wanted to share with you what I got done and the ideas I had on how the process of this project should be from my point of view. 

I have run the server through command prompt by using the following command "python manage.py runserver"
As I also have installed packeges like pip install django,and pip install djangorestframework

Part 1:
To create a backend where a JSON object could be POSTed to create a new customer in the database, I used the Django framework along with Django REST Framework (DRF) to build the API endpoint for handling the POST request.

I set up the Django project by creating a new Django project or using an existing one. This involved running the necessary Django commands or using Django project templates. Once the project was set up, I created an app within the project to handle the customer-related functionality.

I defined the customer model in the app's models.py file. This model represented the structure and fields of the customer object stored in the database. The fields included attributes such as name, email, address, and any other relevant information.

I created the customer serializer, which allowed me to convert the JSON data received in the API request into a customer object and vice versa. The serializer specified the model and the fields to include or exclude when serializing or deserializing the data.

I defined the customer view in the views.py file. This was either a class-based view or a function-based view that handled the POST request for creating a new customer. The view received the JSON data sent in the request, validated it using the serializer, and created a new customer object if the data was valid. If there were any errors in the data, appropriate error messages were returned.

I configured the URL by mapping the URL pattern for the customer creation endpoint to the corresponding view. This was done in the app's urls.py file or the project's urls.py file. The URL pattern specified the endpoint URL where the POST request should be sent.

I handled the POST request. When a POST request was made to the specified URL endpoint, Django's URL routing mechanism directed it to the customer view I had defined earlier. The view deserialized the JSON data, validated it using the serializer, and created a new customer object in the database if the data was valid. Any errors or success messages were returned as an appropriate HTTP response.

By following these steps, I created a backend where a JSON object could be POSTed to create a new customer in the database. This provided a simple yet powerful API endpoint for adding customer data to the system.

Part 2:
To create a second endpoint where a JSON object can be POSTed to create an insurance quote for the customer, I continued building upon the existing Django project and Django REST Framework (DRF) setup. Here are the steps I followed:

Define the insurance quote model:
In the app's models.py file, I defined an insurance quote model that represented the structure and fields of an insurance quote. This model would include fields such as coverage amount, premium, policy details, and a foreign key relationship to the customer model to associate the quote with a specific customer.

Create the insurance quote serializer:
I created a serializer specifically for the insurance quote model. This serializer would handle the serialization and deserialization of JSON data for insurance quotes. It would define the fields to include or exclude when converting the data to and from JSON format.

Define the insurance quote view:
In the views.py file, I defined a class-based or function-based view that handled the POST request for creating an insurance quote. This view received the JSON data sent in the request, validated it using the insurance quote serializer, and created a new insurance quote object associated with the relevant customer in the database.

Configure the URL for the insurance quote endpoint:
In the app's urls.py file or the project's urls.py file, I added a URL pattern for the insurance quote creation endpoint. This pattern specified the URL where the POST request for creating an insurance quote should be sent.

Handle the POST request for insurance quotes:
When a POST request was made to the specified URL endpoint, Django's URL routing mechanism directed it to the insurance quote view that I had defined. The view deserialized the JSON data, validated it using the serializer, and created a new insurance quote object associated with the appropriate customer in the database.

By following these steps, I created a second endpoint where a JSON object could be POSTed to create an insurance quote for a customer. This allowed for the creation of insurance quotes associated with specific customers, expanding the functionality of the backend API.

Part 3:
To implement search functionality for customers and policies based on name, date of birth (DOB), or policy type, I expanded the existing Django project and made the necessary changes. Here's how I approached it:

Modify the customer model:
In the customer model defined earlier, I added fields for name and date of birth (DOB) if they were not already present. These fields would allow me to search for customers based on their name or DOB.

Implement search APIs:
I used a api.py file to define the API endpoints responsible for handling the search functionality for customers and policies separately. These API endpoints would receive the search parameters as query parameters in the URL and perform the corresponding search operations.

Implement customer search:
Within the customer search API, I wrote logic to handle the different search scenarios. If the search query contained a name parameter, I queried the customer model using the name field to find customers with matching names. If the search query contained a DOB parameter, I performed a similar query based on the DOB field. I used Django's query syntax and filters to retrieve the relevant customer records.

Implement policy search:
In the policy search API, I handled the search query parameters related to policy type. If a policy type parameter was present in the search query, I queried the policy model to find policies that matched the specified type. Again, I used Django's query syntax and filters to accomplish this.

Configure the URLs for search endpoints:
In the app's urls.py file or the project's urls.py file, I defined URL patterns for the customer search and policy search endpoints. These patterns specified the URLs where the search requests should be sent and mapped them to the respective search APIs defined in the api.py file.

Handle the search requests:
When a search request was made to the specified URL endpoints, Django's URL routing mechanism directed the request to the corresponding search API. The API processed the search parameters, performed the search operations on the customer or policy models, and returned the matching results as an appropriate HTTP response.

By implementing these steps, I enabled search functionality for customers and policies based on name, DOB, and policy type. Users could now send search requests with the relevant parameters, and the backend would retrieve the matching customer or policy records, providing a powerful search capability within the Django project.

Part 4:
Here's a discussion of how I would implement authentication for users and customers in a Django project:

To implement authentication for users and customers, I would utilize Django's built-in authentication system along with Django REST Framework (DRF) for handling authentication in the API endpoints.

For user authentication, I would leverage Django's user model (django.contrib.auth.models.User) and its authentication APIs. This would include creating views for user registration, login, and password management. I would define a user registration view to capture user details such as username, email, and password, and create a new user object using Django's authentication APIs. Similarly, I would create a user login view to authenticate the user's credentials and generate an authentication token or session.

To enhance security and provide additional features, I would implement password reset and change views by customizing Django's built-in views and forms. These views would allow users to reset their passwords or change them when needed. I would also apply authentication decorators, such as @login_required, to protect specific views that should only be accessible to authenticated users.

Regarding customer authentication, I would follow a similar approach as user authentication but with adjustments to accommodate the specific requirements of customers. This might involve using a different model, such as Customer, to represent customers in the system. I would create views for customer registration and login, tailored to the customer-specific authentication logic. I would also apply authentication decorators to protect customer-specific views that require authentication.

While implementing authentication for users and customers, I would utilize Django REST Framework's authentication mechanisms. These could include token authentication, session authentication, or JWT authentication to secure API endpoints. These mechanisms can be applied to both user and customer authentication, depending on the project's needs.

It's important to consider any additional requirements specific to the application, such as permissions, role-based access control, or integration with external authentication providers. By addressing these aspects, I would ensure a robust and secure authentication implementation for both users and customers in the Django project.


Thank you
