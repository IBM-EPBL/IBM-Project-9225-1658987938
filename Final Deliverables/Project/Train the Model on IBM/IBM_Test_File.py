#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import requests

import json
# NOTE: you must manually set API_KEY below using information retrieved from your IBM Cloud account.
API_KEY = "H3ZSwhKcbaPPAmxup7UnpF9FBPEBXJHbaaa-yUeIJpJU"
token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey":
 API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
mltoken = token_response.json()["access_token"]

header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

# NOTE: manually define and pass the array(s) of values to be scored in the next line
payload_scoring = {"input_data": [{"field": [["do","ph","co","bod","tc","na"]], "values": [[6.7, 7.5, 203, 2, 0.1, 27.0]]}]}


response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/ml/v4/deployments/b6831db5-17e8-4f64-87a2-56aa167b55a9/predictions?version=2022-11-16', json=payload_scoring,
 headers={'Authorization': 'Bearer ' + mltoken})
print("Scoring response")
predict = response_scoring.json()
val = (predict['predictions'][0]['values'][0][0])
print(val)

