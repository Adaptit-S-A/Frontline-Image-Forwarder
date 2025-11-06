## Setup
The web service was tested and deployed on **CentOS 7** using **Python 3.10.13**, with the required libraries listed in the `requirements.txt` file.

## Functionality
Deploy the endpoint:
"https://HOSTNAME:PORT/upload-image", where HOSTNAME & PORT are constants defined in `data.py` file.

## Prerequisites
The **Frontline Server Endpoint** operates only over secure protocols, so an **SSL certificate** is required for the specified `HOSTNAME`.