# Project Title

LOG INGESTOR AND QUERY (FILTER) INTERFACE

# Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)


# Introduction

I've developed my project using  **PYTHON and DJANGO REST FRAMEWORK** to create three interconnected web subsystems. Additionally, I've focused on UI development using fundamental web technologies.

### Log Ingestor:

Developed a POST API to store incoming data in the required JSON format in the database (within our default SQLite DB), ensuring seamless organization and accessibility.

### Log Display:

A dynamic web interface, presenting a comprehensive view of all ingested logs.

### Query Interface:

Empowers users with access to logs and sophisticated filtering capabilities.


# Features

### Log Ingestor:
- Ingest the logs using POST API (In Django we get default SQLLITE DB so logs get stored there)
- URL : [http://127.0.0.1:3000/ingest/]
- JSON :
 ```bash
{
	"level": "error",
	"message": "Failed to connect to DB",
    "resourceId": "server-1234",
	"timestamp": "2023-09-15T08:00:00Z",
	"traceId": "abc-xyz-123",
    "spanId": "span-456",
    "commit": "5e5342f",
    "metadata": {
        "parentResourceId": "server-0987"
    }
}
```
- Sample CURL :
```bash
  curl --location 'http://127.0.0.1:3000/ingest/' \
--header 'Content-Type: application/json' \
--data '{
	"level": "error",
	"message": "Failed to connect Test",
    "resourceId": "server-1234",
	"timestamp": "2023-11-19T08:00:00Z",
	"traceId": "abc-xyz-123-TEST",
    "spanId": "span-456",
    "commit": "5e5342f",
    "metadata": {
        "parentResourceId": "server-0987"
    }
}
```


### Log Display :

- An additional part that I developed to list all the logs that have been ingested till now in the form of a table.
- URL : [http://127.0.0.1:3000/display-logs/]


### Query Filter Interface  :

- This system helps in filtering logs.
- URL : [http://127.0.0.1:3000/query/]


# Installation

Step-by-step instructions on how to install this project:

```bash
# Clone the repository
git clone https://github.com/dyte-submissions/november-2023-hiring-AbhimanyuCODER.git

# Navigate to the folder -> Log_ingestor_and_quey_interface :
cd .\Log_Ingestor_and_Query_Filter\

# Create and Activate a Virtual Environment (If you already having one no need to do this)

# Install the libraries listed in a requirements.txt file.
cd path/to/your/project
pip install -r requirements.txt

# Do migrations using the below commands:
python manage.py makemigrations
python manage.py migrate

# Run the server locally using:
python manage.py runserver

# Now run the URL mentioned below to use the system
INGTEST LOG :  [http://127.0.0.1:3000/ingest/]
DISPLAY LOG :  [http://127.0.0.1:3000/display-logs/]
QUERY INTERFACE :  [http://127.0.0.1:3000/query/]

```
