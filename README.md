# Task_6_Contact_Manager

## Overview

This project contains a Contact Manager application developed using Python. It allows users to manage contacts by adding, updating, deleting, searching, and listing contact records. The program also validates user input to ensure data consistency and prevent duplicate entries.

## Contact Manager Application

### Features

Add new contacts with:

- Unique ID
- Full Name
- Phone Number
- Email Address
- Role (Student, Staff, or Parent)
- Update existing contact details
- Delete contacts by ID
- Search for contacts using their ID
- View all saved contacts
- Prevent duplicate IDs, phone numbers, and email addresses
- Validate phone numbers, email addresses, and user roles

### How it Works

- User selects an option from the main menu.
- Contact information is stored in a dictionary using the contact ID as the key.
- Phone numbers and email addresses are stored in sets to ensure uniqueness.
- Users can update specific fields of an existing contact.
- Users can search for or delete contacts using their unique ID.
- The program continues running until the user chooses to exit.

## Concepts Used

- Loops (while and for)
- Conditional statements (if, elif, else)
- Dictionaries
- Sets
- Lists
- Nested dictionaries
- Input validation
- String methods (upper(), lower(), title(), capitalize())

## Tools Used

- Python
- Visual Studio Code
