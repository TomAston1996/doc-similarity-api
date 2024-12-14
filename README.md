[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

# 📄 Document Similarity API

The goal of Document Similarity API is use Natural Language Processing (NLP) to find similar documents based on the cosine similary score of the document title and it's textual contents.
The problem this is trying to solve is replication in the work place. Often, work is replicated and the context of historical work could aid in delivering new work more quickly.

The plan is to use the SpaCy library to preprocess and calculate vector values for all documents uploaded to a Documents table. 
When a user searches for a similarity match for any new documents the API should return any simialrity matches.

## 🧑‍💻 Tech Stack

![Python]
![FastAPI]
![Postgres]
![Docker]

## 🔧 Setup

### 📋 Dependencies
Run the command ```pip install -r requirements.txt``` to install dependencies.

### 🐋 Docker
Docker Engine is required to run the PostreSQL database.
Download docker desktop [here](https://www.docker.com/products/docker-desktop/).

Run ```docker-compose --env-file .env up --build``` from your root directory to build and run your docker image from the Dockerfile

### ⚙️ Environment
Set up your environment variables in a ```.env``` file which should look similar to the below:
```
POSTGRES_PASSWORD=<db_password>
POSTGRES_DB=<db_name>
POSTGRES_USER=<db_user>
POSTGRES_HOST_PORT=<db_host_port>
POSTGRES_HOST_NAME=<db_host_name>
```

## 🧑‍🤝‍🧑 Developers 

| Name           | Email                      |
| -------------- | -------------------------- |
| Tom Aston      | mailto:mail@tomaston.dev     |

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/TomAston1996/doc-similarity-api-frontend.svg?style=for-the-badge
[contributors-url]: https://github.com/TomAston1996/doc-similarity-api-frontend/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/TomAston1996/doc-similarity-api-frontend.svg?style=for-the-badge
[forks-url]: https://github.com/TomAston1996/doc-similarity-api-frontend/network/members
[stars-shield]: https://img.shields.io/github/stars/TomAston1996/doc-similarity-api-frontend.svg?style=for-the-badge
[stars-url]: https://github.com/TomAston1996/doc-similarity-api-frontend/stargazers
[issues-shield]: https://img.shields.io/github/issues/TomAston1996/doc-similarity-api-frontend.svg?style=for-the-badge
[issues-url]: https://github.com/TomAston1996/doc-similarity-api-frontend/issues
[license-shield]: https://img.shields.io/github/license/TomAston1996/doc-similarity-api-frontend.svg?style=for-the-badge
[license-url]: https://github.com/TomAston1996/doc-similarity-api-frontend/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/tomaston96
[Python]: https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54
[FastAPI]: https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi
[Postgres]: https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white
[Docker]: https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white
[Redis]: https://img.shields.io/badge/redis-%23DD0031.svg?style=for-the-badge&logo=redis&logoColor=white
