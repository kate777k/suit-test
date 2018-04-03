# suit-test
BDD `behave` test suite for a specific e-commerce website

# Introduction

Most Ecommerce sites have the same set of general features:
- Shopping cart
- Checkout
- Product detail page
- Product list page
- Search
- Account page

This example `behave` testsuite contains test scenarios that in general match the functionality of most e-commerce websites

# Setup

## General

- Make sure you have python3.6 or later installed.
- Make sure you have chrome installed
- Create virtual environment:

      $ python3.6 -m venv .venv

- Install required libraries defined in the requirements.txt:

      $ .venv/bin/pip install -r requirements.txt

- Run behave from virtualenv:

      $ .venv/bin/behave
