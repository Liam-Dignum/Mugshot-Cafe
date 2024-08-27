# Mugshot Coffee

## Elevator pitch

Mugshot Coffee is developing a sophisticated ETL (Extract, Transform, Load) pipeline to efficiently process and analyse transaction data. Our cloud-based solution leverages Amazon Web Services (AWS) to provide real-time insights for shop owners to enhance decision-making and business performance.



## Team members

- Liam D
- Alina A
- Colvin S
- Alex H
  
## Project overview

Our ETL pipeline processes data through the following stages:

1. Extract: Retrieve data from CSV files which are uploaded to an S3 bucket
2. Transform: Normalise and clean the data in ExtractTransform Lambda.
3. Load: Data is sent to Load Lambda, which is then sent to a Redshift database
4. Visualise: Present insights through Grafana dashboards

## Architecture (needs to be updated)

![test](https://github.com/generation-de-nat2/Mugshot-Coffee/blob/main/graph%20crop.png?raw=true)

Our solution utilizes the following AWS components:

- S3: For storing raw CSV files
- Lambda: For ETL processing
- Redshift: As our data warehouse
- Cloudformation: To initialise infrastructure (bucket and Lambda) from .YAML template
- EC2

## Repository structure (needs to be cleaned up)

```
Mugshot-Coffee/
├── .github/
│   └── workflows/
│       └── action.yml
├── .vscode/
├── Data/
│   ├── leeds_09-05-2023_09-00-00.csv
│   └── cloudformation/
├── __pycache__/
├── lambda-layer/
│   └── python/
├── .env
├── Main.py
├── README.md
├── config.py
├── connect.py
├── connect_db.py
├── database.ini
├── database.sql
├── docker-compose.yml
├── graph crop.png
├── lambda.py
├── lambdatemplate.yaml
├── main2.py
├── test_unit_tests.py
├── transactions_data.csv
```
### Folder/Files Description

 - .github/: GitHub workflows and actions
 - .vscode/: Visual Studio Code settings.
 - Data/: Contains raw and sample data files
 - lambda-layer/: Python libraries for Lambda functions.
 - .env: Environment variables configuration.
 - Main.py: Main entry point of the application.
 - config.py: Configuration settings.
 - connect.py: Database connection utilities.
 - database.ini: Database configuration file.
 - database.sql: SQL scripts for database setup.
 - docker-compose.yml: Docker Compose configuration.
 - lambda.py: Lambda function code.
 - lambdatemplate.yaml: AWS CloudFormation template for Lambda functions.
 - test_unit_tests.py: Unit tests for the application.
 - transactions_data.csv: Sample transaction data.

## Getting Started

### Prerequisites

- Docker
- AWS CLI
- Python 3.12+

### Local setup

1. Clone the repository
   - git clone https://github.com/generation-de-nat2/Mugshot-Coffee.git
   - cd Mugshot-Coffee
2. Set up envirnment variables
3. Install dependecies.
   - pip install -r requirements.txt
4. Run docker compose
   - docker-compose up
5. Deploy infrastructure (use aws cloudformation )
   - aws cloudformation create-stack --stack-name mugshot-coffee --template-body file://lambdatemplate.yaml
6. Run the application
   - python Main.py

### License
This project is licensed under the MIT License. See the LICENSE file for details.
