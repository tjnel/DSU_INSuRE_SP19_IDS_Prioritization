# IDS Alert Prioritization and Strengthening 
#### Bikram Dangi, Jeremy Gamet, Arica Kulm, TJ Nelson
#### Dakota State University

## Project Description
We researched data science and machine learning techniques that can be used to fine tune an Intrusion Detection System (IDS).  The goal of this research was to create a working prototype to aid in the reduction of customizations organizations need to make when implementing and maintaining a working and effective IDS.  This prototype could then be further enhanced by future research teams.

## Research Problem
IDS require extensive and continuous adjustments for the specific network they are deployed on.  Efforts are needed to reduce the high number of false positives that signatures are generating.  These false positives lead to analysts spending much of their time in assessment or simply turning them off to avoid the distraction which then leaves their systems vulnerable.

## Objectives
We are seeking a way to combine these weak, high-false-positive signatures to generate low-false-positive strong indicators.  We seek to do this by: Exploring the nature of these low priority alerts to determine which combinations produce a strong indicator of intrusion. Determining any currently established models for pattern recognition. In the absence of a working model, creating our own model for testing. Use this working model to then apply data analysis techniques to look for unknown patterns. And finally, testing this working model against another large dataset with the intention of validation of our implementation for possible future use in an open source IDS platform.

## Dataset Note
The two datasets being used for testing and validation are CSE-CIC-IDS2018 on AWS and Intrusion Detection Evaluation Dataset (CICIDS2017). Both of which can be found at https://www.unb.ca/cic/datasets/
*Note* The flow data *.csv files found in CSE-CIC-IDS2018 and IDS2017 are quite large, with the 2018 data being well over 8GB in memory. It is therefore advised to run these Jupyter Notebooks with a runtime which is able to handle quite a bit more than 8GB of data in memory at one time.

## Order of use
We studied the data with the four notebooks contained in this Git Repo. The initial exploration was done first with CSC791_IDSML_Initial_K_Means_Data_Exploration_and_Visuals.ipynb upon a small subset of the data in order to determine some fundamental paterns within the dataset.

Next we use CSC791_IDSML_Dataset_Ingestion.ipynb to start aggregating the dataset from IDS2018 into a single larger Dataframe using pandas.

After this we use CSC791_IDSML_TrainTest_Split.ipynb to further clean and normalize the data as well as split it into a training group and a testing group.

After splitting and cleaning the data we use CSC791_IDSML_Classifiers.ipynb to run our decision tree classification training and then confirm our accuracy scores and create a prioritization score based on the probabilities found with our decision tree models.

Then last we validate the success of our classifier on the CIC-IDS2017 Dataset.
