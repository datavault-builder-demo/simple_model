import base64
import requests
import zipfile
import os
import shutil
import os

deploy_user = 'dvbadmin'
deploy_password = 'eeyvdclsyaAB!123' 
deploy_baseUrl = 'http://localhost:81/cicd/'
######################################################################## read from folder

with zipfile.ZipFile('../model/model_export.zip', 'r') as zip_ref:
    zip_ref.extractall('model_export')


######################################################################deploy    
    
    # prepare cicd model export api call
payload = {"username": deploy_user,"password": deploy_password,
	"dependencies_state_up_to_date": {"timeout_in_seconds": 50, "cancel_on_timeout": False}, 
    "source_environment": {
		"environment_type": "file",
		"environment_parameters": {
			"model_zip_base64_encoded" : base64_zip_string }, #here we pass the string we received in step one
		},
    "target_environment": {
        "environment_type": "local",
		"environment_parameters": {
		#	"url": "http://host.docker.internal",
		#	"username": "dev",
		#	"password": "welcome@DVB!"
		}
	}}
headers = {'Forwarded':'by=webgui;for=webgui;host=webgui;proto=http','Content-Type':'application/json'}

# call api and retrieve encoded zip content
res = requests.post(deploy_baseUrl + 'deployModel', json=payload, headers=headers)
jsonBody = res.json()
print(jsonBody)