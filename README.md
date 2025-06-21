#  Notification System (Abstract Inheritance in Python)

This project demonstrates the use of **abstract base classes**, **inheritance**, and **polymorphism** in Python using a simple notification system.

##  Features

- Defines an abstract base class `Notification` with an abstract method `send()`.
- Implements three child classes:
  - `SMS` with a `carrier` attribute
  - `Email` with an `email_provider` attribute
  - `Push` with a `device_type` attribute
- Each subclass overrides the `send()` method and formats the message output differently.
- Includes test cases that create instances and send personalized messages.

##  Concepts Covered

- Abstract base classes (`ABC`)
- Inheritance and method overriding
- Class attributes and constructors
- Basic polymorphism

