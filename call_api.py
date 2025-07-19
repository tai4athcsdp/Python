# Use the requests library to simplify making a REST API call from Python 
print("Hello world!")
import requests

# # We will need the json library to read the data passed back 
# # by the web service
import json

# # You need to update the SUBSCRIPTION_KEY to 
# # they key for your Computer Vision Service
SUBSCRIPTION_KEY = "3nEhBGfPOGlVKNN434OQFmBbzAvFWPmLBagN55yIRMM"

# # Add the name of the function you want to call to the address
address = "https://api.unsplash.com/photos/?client_id=" + SUBSCRIPTION_KEY

# # we use HTTP GET to call this function
response = requests.get(address)

# Raise an exception if the call returns an error code
response.raise_for_status()

# Display the JSON results returned
results = response.json()
print(json.dumps(results))