7Homework Management System

Project Description

Homework Management System is a standalone Python application designed to help students efficiently organize, track, and manage their homework tasks in one centralized system.

The application allows users to:

• Add and manage homework tasks, including title, description, subject, and deadline.

• Create and organize subtasks for each homework activity.

• Automatically assign priority levels based on due dates using a Priority Engine.

• Mark homework tasks as completed and monitor their status.

• Generate summary reports showing total homework, completed tasks, pending tasks, overdue tasks, and completion rates.

Built with a simple Command-Line Interface (CLI), the system emphasizes usability, efficiency, and accessibility. The application operates entirely offline and follows a structured Input → Process → Output model, ensuring reliable performance without requiring external databases or internet connectivity.

Through this application, students can improve time management, monitor academic responsibilities, avoid missed deadlines, and maintain productivity throughout their studies.

OOP Concepts Used

This project demonstrates core Object-Oriented Programming principles:

Encapsulation

Data and behaviors are organized within classes such as Homework, Validation, PriorityEngine, and ReportGenerator.

Abstraction

Each class focuses on a specific responsibility, simplifying the overall system design.

Polymorphism

Methods such as display() and generate_report() perform different operations depending on the object and context in which they are used.

Modularity

The program is divided into separate classes that handle homework management, validation, priority assignment, and report generation.

Technologies Used

• Python 3

• Command-Line Interface (CLI)

• Date and Time Handling using Python's datetime module

• Object-Oriented Programming (OOP)

Main Features

Feature 1 – Add Homework

Allows users to enter homework details including title, description, subject, deadline, and subtasks.

Feature 2 – Homework Validation

Validates required fields and ensures the deadline follows the YYYY-MM-DD format.

Feature 3 – Automatic Priority Assignment

Uses the Priority Engine to determine whether homework is LOW, MEDIUM, HIGH, CRITICAL, or OVERDUE.

Feature 4 – View Homework

Displays all homework records along with their details, priorities, and completion status.

Feature 5 – Mark Homework as Done

Allows users to update homework status from Pending to Completed.

Feature 6 – Generate Report

Creates a summary report showing total homework, completed tasks, pending tasks, overdue tasks, and completion percentage.

Project Structure

Homework-Management-System/

│

├── homework_management_system.py

├── README.md


How to Run

Requirements

Python 3.x

Clone this Repository

git clone
https://github.com/aldredmon54-bot/Homework-Management-Application

Navigate to the Project Folder

cd Homework-Management-Application

Run the Application

python homework_management_system.py

Sample Menu

1. Add Homework

2. View Homework

3. Mark Homework as Done

4. Generate Report

5. Exit

Author

Aloha Jil Gozarin (https://github.com/gozarinalohajil)

Rhandie Mari Guan

Aldred C. Valdez (https://github.com/aldredmon54-bot?tab=repositories)


This project demonstrates the application of Object-Oriented Programming principles through the development of a Homework Management System that helps students efficiently manage academic tasks and deadlines.