# jinja_workflow_example [![v0.0.1](https://img.shields.io/badge/version-0.0.1-blue.svg)](https://github.com/uchicago-library/jinja_workflow_example/releases)

[![Build Status](https://travis-ci.org/bnbalsamo/jinja_workflow_example.svg?branch=master)](https://travis-ci.org/uchicago-library/jinja_workflow_example) [![Coverage Status](https://coveralls.io/repos/github/uchicago-library/jinja_workflow_example/badge.svg?branch=master)](https://coveralls.io/github/uchicago-library/jinja_workflow_example?branch=master)

A repository for testing jinja facilitated workflows with a dedicated front end team

# Scenario

I have developed a new "killer app" - a combination of a beloved television show, as well as social and professional networking sites.

This site is a static social network for fictional people who work in the same office, and who have posted gibberish in Latin.

People can spend hours browsing this content - I imagine it will replace Facebook, LinkedIn, Game of Thrones, and Latin 1 coursework in high schools across the world in the near future.

Unfortunately, despite it being packed with engaging content, the web UI is (almost) non-existent. 

I have created a barebones web UI for displaying this data, and will happily provide new routes, or alter existing routes, in order to work together
to create a interface through which to present this information.

# Installation

```
$ git clone https://github.com/bnbalsamo/jinja_workflow_example.git
$ cd jinja_workflow_example
$ python3 -m venv venv
$ source venv/bin/active
$ pip install -r requirements.txt
$ python setup.py develop
```

# To spin up a Dev Environment

```$ ./debug.sh```

or

```
$ docker build . -t jinja_experiment
$ docker run -p 5000:80 jinja_experiment
```

or

However else you want to run a flask debug server or containerized webserver

After doing that, pointing a browser at http://localhost:5000 should display a web page, and http://localhost:5000/p/0 should show a profile

# First Steps

- Skim [the relevant portions of the jinja docs](http://jinja.pocoo.org/docs/2.10/templates/) 
- Take a look at ```./jinja_workflow_example/blueprint/__init__``` to see how routes are defined, and how variables get passed to templates 
- Take a look in the ```./jinja_workflow_example/blueprint/templates/``` folder and try playing around with the templates to change the appearance of pages.
- Hypothesize what other information would be nice to have fed into the templates, and what the requirements of different routes/pages/templates might be.
- Have a look at the template hierarchy itself, to see if it would benefit from more abstraction or more granularity.


# Author
Brian Balsamo <brian@brianbalsamo.com>, 2018-02
