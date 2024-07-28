Jules Test UI automation
1. Introduction
This project is all about e2e test automation framework  using Selenium-Webdriver for UI automation, python for scripting and pytest for creating e2e test framework.

The framework is following POM(Page object pattern) design pattern.

2. Pre-requisite/Environment set-up
First you need to clone the repo on your local using below command:

git clone  https://github.com/SaurabhP26k97/jules-ai
Then you need to install packages using pip(use pip3 for mac) command. Run the command below in terminal:

a. Install python:

$ brew install python

b. install Selenium

$ pip3 install python

c. install pytest

$ pip3 install pytest

d. pip3 install Webdriver-manager:

$ pip3 install webdriver-manager

3. Project Features->
framework follows page object pattern
data-driven tests
tests can be run on popular browsers - Chrome and Firefox are prconfigured in DriverFactory class and both can be select in conftest.py
4. Running Tests
To run tests, run the following command

  pytest file_name.py
