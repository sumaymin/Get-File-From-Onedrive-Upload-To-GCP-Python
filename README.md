# Get File From Onedrive And Upload To GCP Via Python

Hi, I gonna show how do I access and get file from OneDrive via Python. In detail of access and list files from OneDrive, you can see more detail in 
https://github.com/pranabdas/Access-OneDrive-via-Microsoft-Graph-Python from pranapdas. 
I apply and add datetime conditions about created datetime and last modified date and file condition for getting specific files. 
After got all files, I gonna load these files to the bucket in GCP. 

# Get Access Token From POSTMAN 
In this project, I used POSTMAN. You can choose Authorization field and select OAuth 2.0 then you fill about details of App Register from Azure and click 'Get New Access Token'. The Example of POSTMAN is show below
<img width="640" alt="image" src="https://user-images.githubusercontent.com/90255313/204963259-7190e29b-7930-48fb-8633-6a8bfdf7ea1c.png">
