# Currency Exchange Rate Data Acquisition and Preprocessing Pipeline

## Background

The Currency Exchange Rate Data Acquisition and Preprocessing Pipeline is a project designed to automate the retrieval, preprocessing, and storage of currency exchange rate data. This pipeline aims to streamline the process of obtaining up-to-date exchange rates for various currency pairs.

The need for accurate and timely exchange rate data is crucial for financial institutions, businesses, and individuals involved in international trade and finance. This project addresses this need by leveraging APIs to fetch real-time exchange rate information and preprocess it for storage in a database.

## Requirements

The project's primary objectives are:

1. **Data Acquisition**:
   - Implement a data acquisition module to retrieve currency exchange rate data from a chosen API.
   - Allow users to input the base and target currencies for which they want to obtain exchange rates.
   - Ensure proper error handling in case of API request failures.

2. **Preprocessing and Transformation**:
   - Normalize the acquired exchange rates to a standardized format (e.g., rounding to a fixed number of decimal places).
   - Validate the data to ensure it meets the required criteria for storage.

3. **Database Integration**:
   - Establish a database schema to store exchange rate data.
   - Implement functions for inserting and retrieving data from the database.
   - Ensure data integrity and handle potential exceptions during database interactions.

4. **Demonstration**:
   - Create a user-friendly script that guides users through the process of acquiring, preprocessing, and storing exchange rate data.
   - Provide clear prompts for user input and appropriate feedback for each step.

Additionally, the project must adhere to the following technical requirements:

- Use Python 3.12 for development.
- Utilize a Git repository for version control and documentation management.
- Maintain clear and concise documentation in plain text format (.md) within the repository.

The completion of this project will result in an automated pipeline that facilitates the acquisition and preprocessing of currency exchange rate data, ultimately enhancing the efficiency of tasks related to currency conversion and financial analysis.
