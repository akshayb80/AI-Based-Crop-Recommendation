# AI-Based-Crop-Recommendation
This project is a under the AI/ML track. The purpose of this project is to show a suitable crop to grow, 
given the physical conditions of the farm which include Soil Nitrogen, Soil Phosphorus, Soil potassium
, Rainfall, Humidity, soil pH and Temprature.

# Developed By:
* Akshay Bakshi
* Prasad Thakare
* Nikhil Sharma

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
Accuracy: 90.454<br/>
can be found in python_notebooks/Model.ipynb 

### K-Nearest-Neighbours
Accuracy: 97.818<br/>
can be found in python_notebooks/model knn.ipynb

### Ensembled model 
A model is created by ensembling together Decision Trees, K-Nearest-Neighbours, Random Forests and Support Vector Machine<br/>
Final Prediction is considered as the majority vote of all models.<br/>
Accuracy: 98.728<br/>
can be found in python_notebooks/ensemble.ipynb

### Thus, the ensembled model is considered for Deployment

# Installation

* Clone the main branch of this repository
* Install all the dependencies using
```pip install -r requirements.txt```
* Use ```python app.py``` command in the root directory to start the flask server
* The site would be served on the localhost:5000

# Screenshots:

![image](https://user-images.githubusercontent.com/56474333/102004417-711a2800-3d36-11eb-874d-182b5ee108ce.png)

![image](https://user-images.githubusercontent.com/56474333/102004481-29e06700-3d37-11eb-8e6a-d2807b708fa7.png)




