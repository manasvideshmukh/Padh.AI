# Padh.AI

Padh.AI is a platform which is like a teacher who knows everything about their students and accordingly teaches them concepts. The platform creates roadmaps for particular topics, generates flashcards to understand the topic thoroughly, conduct quizzes on any topic and analyze the result of the quizzes to guage the understanding of the student . Study buddies study the exact same topics and have a leaderboard to compete with each other. This is all about Padh.AI, a virtual tutor platform.


`

## Setup

The first thing to do is to clone the repository:

```sh
$ git clone  https://github.com/manasvideshmukh/Padh.AI
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ virtualenv venv
$ source venv/bin/activate
```

Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```
Note the `(env)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `virtualenv2`.

Once `pip` has finished downloading the dependencies:
```sh
(env)$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000/`.

`