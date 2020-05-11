# Mood Sing API

This is a Flask API that returns a hexademical color representation based Spotify user's recent listening history. 
This API works in conjunction with the [Mood Ring UI](https://github.com/aasthakhanna/mood-sing-ui).

## Local Setup
1.) Install npm


2.) Install Python3, pipenv, and Flask


3.) Install [Serverless](https://www.serverless.com/framework/docs/getting-started/)


4.) Run "pipenv install" and "npm install" to install dependencies on your local machine

## Endpoints
This API has one endpoint, GET /getColor. It expects a Bearer token, provided as an Authorization header, that will allow it to access Spotify's API. The client is responsible for providing this authorization.
[Spotify's guide on authorization](https://developer.spotify.com/documentation/general/guides/authorization-guide/)

## Deployment
This API uses Serverless, which deploys code from your local environment to an AWS lambda using CloudFormation templates. It exposes the endpoints on AWS API Gateway and hosts them on a domain for easy access.
To deploy: ``sls deploy``
