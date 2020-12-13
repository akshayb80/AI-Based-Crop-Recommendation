# AI-Based-Crop-Recommendation
This project is a under the AI/ML track. The purpose of this project is to show a suitable crop to grow, 
given the physical conditions of the farm which include Soil Nitrogen, Soil Phosphorus, Soil potassium
, Rainfall, Humidity, soil pH and Temprature.

# Technologies

* ML Model Development:
  * Scikit-Learn
  * Pickles
  * Numpy
  * Pandas
  
* Web Development:
  * Flask (Backend)
  * Basic HTML/CSS/JS (Frontend)

# Algorithms
The dataset 'CropDataset.csv' has been used for the creation and testing of the AI models. An instance of the same is shown below:
The complete dataset can be found in the python_notebook directory of the repository

<img width="567" alt="Untitled" src="https://user-images.githubusercontent.com/56474333/102003799-af144d80-3d30-11eb-81b3-34d56a819bd9.png">

The dataset has been used to train the following models and the corresponding accuracies have been obtained:
### Decision Trees
Accuracy: 90.45454545454545
can be found in python_notebooks/Model.ipynb 

### K-Nearest-Neighbours
Accuracy: 97.81818181818181

### Ensembled model 
A model is created by ensembling together Decision Trees, K-Nearest-Neighbours, Random Forests and Support Vector Machine
Final Prediction is considered as the majority vote of all models.
Accuracy: 98.72

### Thus, the ensembled model is considered for Deployment

# Installation
* Clone the main branch of this repository
* Install all the dependencies using
```pip install -r requirements.txt```

