# Email Sending Project with Data Received from Light Sensor
# Overview
During my internship at MİA Teknoloji, I developed a project that continuously monitors data obtained from a light sensor. The system is designed to automatically send a notification email to a predetermined email address when the light sensor data rises above a certain preset value. Additionally, the system records the data at regular intervals, saving it to an Excel file for future analysis and monitoring.

# Features
The Email Sending Project with Data Received from Light Sensor includes the following features:

Continuous Monitoring: The light sensor data is monitored every 3 seconds.

Email Notifications: When the light sensor value exceeds a preset threshold, an email notification is sent automatically.

Data Logging: The received data, along with the relevant date and time, is saved in an Excel file for future reference.

# Technical Details
The project involves the following components and steps:

Hardware Setup: An Arduino board is used to interface with the light sensor and obtain data.

Software Setup: The Arduino IDE is used to program the Arduino board to read data from the light sensor. Python is used for further processing and automation, using tools like PyCharm for development.

Serial Communication: Data is transferred from the Arduino to the computer using serial communication.

Email Sending: Using Python's smtplib, emails are sent when certain conditions are met.

Data Logging: Python's openpyxl library is used to record the data in an Excel file.

# Conclusion
This project provided valuable experience in hardware-software integration, serial communication, and automation using Python. It demonstrates the practical application of these skills in creating an automated monitoring and notification system.
