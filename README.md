You are supposed to construct a data engineering pipeline through Airflow and perform
versioning of the datasets through DVC.
Objective
The aim of this activity is to provide students with practical experience on:
Using DVC (Data Version Control) for managing datasets and machine learning models.
• Implementing data versioning and model versioning using DVC.
• Streamlining workflows using Airflow.
Instructions
You will build a pipeline to gather weather data via API (any of your choice but the data
should be live data), preprocess the data, version-control it using DVC, train a simple
machine learning model, try to create workflow through DVC and version it.
Steps
Setting Up the Environment and Data Collection
1. Set up your project:
- Create a Git repository for your project.
- Initialize DVC in your project folder (`dvc init`).
- Set up a remote storage location for DVC (e.g., Google Drive, S3, or local storage).
2. Data collection:
- Use one of the following methods to collect weather data:
- API: Use i.e., OpenWeatherMap API or a similar service to fetch weather data.
- Collect at least 5 days of weather data with the following fields:

1. Temperature,
2. Humidity
3. Wind Speed
4. Weather Condition
5. Date, and Time.

3. Save raw data:
- Save the collected data in a CSV file (e.g., `raw_data.csv`).
- Use DVC to track this data.

Data Preprocessing and Workflow Automation with Airflow
1. Preprocess the data:
- Handle missing values (if any).
- Normalize or standardize numerical fields (like temperature and wind speed).
- Save the preprocessed data as `processed_data.csv`.
2. Version the processed data:
- Track the preprocessed data with DVC.
3. Automate the workflow with Airflow:
- Set up an Airflow pipeline with two tasks: Data Collection and Data Preprocessing.
- Ensure the pipeline runs end-to-end seamlessly.

Model Training
1. Train a simple model:
- Use a linear regression model to predict temperature based on other features.
- Save the model as a pickle file (e.g., `model.pkl`).
2. Version the model:
- Use DVC to track the model.
3. Create a DVC pipeline:
- Define the steps in a DVC pipeline for data collection, preprocessing, and training.

Important Points
This activity is going to be a group activity, and the group shall include 3 people at max.
Moreover, the work done in this activity will be extended in the project. Once, this activity
gets completed a next document will be uploaded that will describe additional steps that
will be considered as a project. Moreover, I have given weather data as an example, you can
consider any type of data but the data should be live data.
