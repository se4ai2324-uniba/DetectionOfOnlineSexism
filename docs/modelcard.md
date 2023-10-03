# Detection of Online Sexism


## Model Details 
### Basic information about the model.
The project described in this documentation has been developed for the "SemEval 2023 - Task 10 - Explainable Detection of Online Sexism (EDOS)" challenge on CodaLab by Grazia Perna and Maria Elena Zaza, in which two models have been implemented.

Before training these two models a preprocessing phase has been carried out, where there was a custom text cleaning function to remove spaces, convert text to lowercase and eliminate punctuation.There were used other techniques like the tokenization and, in the case of the task A, the lemmatization.
The cleaned text was then fed into a CountVectorizer, which transformed the text into numerical features suitable for classification.

The models have two hierarchical tasks:
- TASK A - Sexism Detection: for detecting whether a post is sexist by using the LinearSVC classifier.
- TASK B - Category of Sexism: for assigning to each of the sexist texts one of the following categories:
    - threats
    - derogation
    - animosity
    - prejudiced discussions

To evaluate the performance of the models the GriSearchCV was employed for performing the hyperparameter tuning in order to determine the optimal values of the models. It uses the Cross-Validation method, fixed to 10.

The project and the paper are available at: https://github.com/graziaperna/NLP-project.

## Intended Use 
### Primary intended uses

This project is intended for commercial and research use in English. The models can be used in several domains:
- Messenger services
- Investigations
- Journalism
- Publishing

### Primary intended users

The primary intended users of this study caters primarily to researchers, practitioners and participants engaged in the field of natural language processing. This audience includes individuals and entities actively involved in the development and implementation of algorithms and models for the detection and categorization of online sexism.

Additionally, participants and researchers involved in similar challenges or projects addressing nuanced language analysis and detection of sensitive content may find our work relevant and insightful.

## Factors 
### Training Factors 

For text processing tasks, TreeBankTokenizer and NLTK libraries were necessary. 
In terms of machine learning, the libraries used were Scikit-learn and NumPy. 
To chain together various steps such as text vectorization and model training, Scikit-learn’s Pipeline class was used. Additionally, two useful libraries were the pandas library for data manipulation and analysis and NumPy for efficient array operations.

## Metrics 
### Metrics should be chosen to reflect potential realworld impacts of the model.
- Model performance measures
- Decision thresholds
- Variation approaches


## Evaluation Data 
### Details on the dataset(s) used for the quantitative analyses in the card.
- Datasets
- Motivation
- Preprocessing


## Training Data 
### May not be possible to provide in practice. When possible, this section should mirror Evaluation Data. If such detail is not possible, minimal allowable information should be provided here, such as details of the distribution over various factors in the training datasets.


## Quantitative Analyses
- Unitary results
- Intersectional results 


## Ethical Considerations


## Caveats and Recommendations