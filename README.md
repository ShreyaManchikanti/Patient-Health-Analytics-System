# Patient Health Analytics System

## Module Information

**Module Name:** Introduction to Programming for Big Data  
**Module Code:** 55-710252-AF-20256  
**Assignment Title:** Recommendation Engine and Exploratory Data Analysis  
**Student Name:** [Your Name]  
**Student ID:** [Your Student ID]

---

# Project Overview

This project implements a Patient Health Analytics System using Python and Object-Oriented Programming (OOP) principles. The system analyses patient health records from the provided dataset and enables clinicians and healthcare analysts to query patient information, generate health statistics, identify risk factors, and produce summary reports.

The system consists of five modules:

1. load_dataset_module.py
2. statistics_module.py
3. query_module.py
4. user_interface_module.py
5. main.py

The application provides a graphical user interface (GUI) built with Tkinter and allows users to export query results into CSV files.

---

# Features

## Dataset Loading and Processing

- Loads patient data from data.csv
- Converts data into appropriate Python data types
- Handles missing or invalid data
- Stores data in memory for analysis

## Statistical Analysis

The system computes:

- Mean
- Median
- Mode
- Standard Deviation
- Variance
- Minimum
- Maximum
- Range

It also provides descriptive statistics for any selected numeric feature.

## Query and Analysis Functions

The system supports the following analyses:

- Average, modal, and median age of smokers with hypertension
- Average age and glucose level of heart disease patients
- Stroke analysis by gender and hypertension status
- Physical activity level analysis
- Urban versus rural stroke analysis
- Dietary habit comparisons
- Identification of patients whose hypertension resulted in stroke
- Identification of heart disease patients who experienced stroke
- Sleep hour comparisons
- Multi-criteria patient filtering
- Stroke risk categorisation
- Regional health summary reports

## Export Functionality

All query results can be exported to CSV format for further analysis.

## Graphical User Interface

The GUI allows users to:

- Select analyses from a menu
- Enter filtering criteria
- View results in a readable format
- Export results to CSV
- View descriptive statistics
- Continue using the system or exit

---

# Project Structure

```text
Task_1/
│
├── data.csv
├── load_dataset_module.py
├── statistics_module.py
├── query_module.py
├── user_interface_module.py
├── main.py
├── README.md
└── presentation.mp4
```

---

# Module Descriptions

## load_dataset_module.py

Responsible for:

- Reading the dataset
- Validating records
- Converting data types
- Returning structured patient data
- Handling file-related exceptions

---

## statistics_module.py

Responsible for:

- Computing statistical measures
- Generating descriptive statistics
- Supporting analysis performed by other modules

---

## query_module.py

Responsible for:

- Filtering patient records
- Generating health insights
- Producing summary reports
- Exporting results to CSV

---

## user_interface_module.py

Responsible for:

- User interaction
- Displaying results
- Accepting input parameters
- Error handling and notifications

---

## main.py

Responsible for:

- Importing all modules
- Initialising the application
- Launching the graphical interface

---

# Object-Oriented Programming Concepts Used

The system has been designed using Object-Oriented Programming principles:

## Encapsulation

Data and related methods are organised within classes.

## Inheritance

Common functionality is reused through inheritance where appropriate.

## Abstraction

Complex operations are hidden behind user-friendly methods.

## Polymorphism

Methods can be extended or overridden to support additional functionality.

---

# Exception Handling

The application includes exception handling for:

- Missing files
- Invalid user input
- Incorrect data types
- Empty datasets
- Export errors

This ensures the application exits gracefully and provides meaningful feedback to users.

---

# Requirements

The following libraries are required:

- Python 3.x
- pandas
- numpy
- tkinter

Install dependencies using:

```bash
pip install pandas numpy
```

Tkinter is included with most Python installations.

---

# Running the Application

Open a terminal inside the project directory and execute:

```bash
python main.py
```

or

```bash
python3 main.py
```

The graphical user interface will launch automatically.

---

# Testing

The application has been tested for:

- Dataset loading
- Statistical calculations
- Query execution
- GUI interaction
- CSV export functionality
- Error handling

---

# Future Enhancements

Potential future improvements include:

- Interactive visualisations
- Database integration
- Machine learning-based stroke prediction
- User authentication system
- Web application deployment

---

# Conclusion

The Patient Health Analytics System demonstrates the application of Object-Oriented Programming, data analysis, statistical computation, exception handling, and graphical user interface design to support healthcare decision-making and patient risk assessment.
