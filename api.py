from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Policy, Customer



@api_view(['GET'])
def test_customer(request):
    print("test_customer function...")
    return Response({'message': 'test message'})

@api_view(['POST'])
def create_customer(request):
    # Process the JSON object received in the request
    data = request.data
    
    # Save the customer object to the database
    # Implement your custom logic here
    
    # Return a response
    return Response({'message': 'Customer created successfully'})

#part 2

@api_view(['POST'])
def create_quote(request):
    data = request.data

    # Extract necessary data from the request JSON
    customer_id = data['customer_id']
    quote_amount = data['quote_amount']

    # Create a new Policy object
    policy = Policy.objects.create(
        customer_id=customer_id,
        quote_amount=quote_amount,
        state='quoted'
    )

    return Response({'message': 'Quote created successfully'})

@api_view(['POST'])
def create_quote(request):
    # Process the quote creation as before

    # Assuming the customer accepts the quote and wants to convert it to a live policy
    policy.state = 'bound'
    policy.save()

    return Response({'message': 'Quote converted to a live policy'})

#part3

@api_view(['GET'])
def search_customers(request):
    query = request.query_params.get('query', '')

    # Search customers by name or DOB
    customers = Customer.objects.filter(
        Q(name__icontains=query) | Q(dob__icontains=query)
    )

    # Serialize and return the search results
    serialized_customers = CustomerSerializer(customers, many=True)
    return Response(serialized_customers.data)

@api_view(['GET'])
def search_policies(request):
    query = request.query_params.get('query', '')

    # Search policies by policy type
    policies = Policy.objects.filter(policy_type__icontains=query)

    # Serialize and return the search results
    serialized_policies = PolicySerializer(policies, many=True)
    return Response(serialized_policies.data) 

from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from .authentication import UserAuthentication, CustomerAuthentication

@api_view(['GET'])
@authentication_classes([UserAuthentication])
@permission_classes([IsAuthenticated])
def protected_view(request):
    # Only authenticated users can access this view
    # ...

@api_view(['GET'])
@authentication_classes([CustomerAuthentication])
@permission_classes([IsAuthenticated])
def customer_protected_view(request):
    # Only authenticated customers can access this view
    # ...
    