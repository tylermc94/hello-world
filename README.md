# hello-world
Hello World

This repo is where Im going to store anything related to my python learning journey

## todo.py
This is a simple to-do list app that I am slowly adding features to with the help of Claude AI as I learn how to use Python. It creates a task list in the form of a dictionary and is able to manipulate it as well as save and load the list in a JSON file, **todolist.json**

## Dimmer Switch.py
A basic dimmer program to run on the Raspberry Pi Pico, mostly vibe coded. It just takes input from a pot and dims an LED.

## thermostat.py
This was my thought for a good beginner project before I moved to the to-do list. I think I'll still come back to this, it feels like a good way to integrate my Python skills with my microcontroller skills by making a simple thermostat/heat controller with a Pi Pico.

## Pihole-API-top-domains.py
Learning how to use APIs in Python. This pulls the Pihole address and API key from a config file and runs two API GET calls, first to authenticate, then to get the list of top domains visited on my network. It automatically pulls the authentication keys from the auth call response and feeds them to the domain list call, then it formats the top domains list into a decent looking table.
