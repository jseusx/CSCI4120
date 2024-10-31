# Homework 4: Comparing LinearRegression, Lasso, and Ridge models
## Team Members:
Jesus Jimenez-Sanchez <br> 
**Email:** Jimenezsanchezj18@students.ecu.edu
## Required Items:
- Jupyter Notebook
  -   Can be used to run code without IDE
- IDE
  - Install requirements from main branch use the README for help.
- Download the 2 data files under (data)
## Cross Validation scores and Alpha values:
### Lasso
Lasso Best Alpha: {'alpha': 0.11513953993264481} <br>
Laso CV score: 233792.1271999313 <br>
Lasso Test score: 0.8803840481176711
### Ridge
Ridge Best Alpha: {'alpha': 0.5963623316594643} <br>
Rdige CV score: 233739.05385091278 <br>
Ridge Test Score.8799326304260703
### Linear Regression
Linear Regression CV Score: 233807.34994833203 <br>
Linear Regression Test Score: 0.8804570314760505

## Which model performs best?
Ridge will perform the best based on the data as it has the lowest CV value.<br>
It will perform best when it has an alpha value of: 0.5963623316594643, 0.6 if rounded.
