# Instructions

## Assign Required Google Cloud IAM Roles for your service account, in IAM > Service Accounts 

App Engine Admin (roles/appengine.appAdmin). Manages App Engine resources and creates new services and versions. 

Storage Admin (roles/storage.admin). Uploads source code artifacts to Google Cloud Storage. 

Cloud Build Editor (roles/cloudbuild.builds.editor). Executes the container build process for the deployment. 

Artifact Registry Reader (roles/artifactregistry.reader). Retrieves build artifacts during the CI/CD pipeline.

Service Account User (roles/iam.serviceAccountUser). Allows the deployment account to act as the App Engine runtime service account (typically PROJECT_ID@appspot.gserviceaccount.com). 

## Enable the App Engine Admin API for your project 

Under APIs and Services 

## Create a credentials file

IAM > Service accounts 
Dots after default service account > keys
Create new credentials file. Make sure you DON'T add this file to your GitHub repo

## Set up repository secrets 

In GitHub setttings, Security > Secrets and variables > Actions 

Create two new repository secrets, 

GCP_PROJECT_ID, value is your project ID 
GCP_SA_KEY, value is the text from your credential file 

## Create .github/workflows/deploy.yaml file 

Describe how to run tests and how to deploy, and that these happen when you push to main. A merged PR to main also creates a push event so this will run when a PR is merged to main 


