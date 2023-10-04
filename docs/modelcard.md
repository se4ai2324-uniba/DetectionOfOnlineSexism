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

The project, the paper and a simple demo are available at: https://github.com/graziaperna/NLP-project.


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

The accuracy of the results of these models can be influenced by several demographic factors, like the language, the culture, the age and the gender.

## Metrics 
### Metrics should be chosen to reflect potential realworld impacts of the model.

The data were divided into three splits: train, validation and test. As a matter of fact, the models were trained using the train set.
Then the validation set was used to assess their performance and make any necessary adjustments or tuning. Finally, the test set was employed to evaluate the models’ generalization ability and obtain their final performance metrics.
The metric computed were:
- Accuracy
- Precision
- Recall
- f1

For ach of these metrics were considered the macro measure.
In the following table the model performance measures computed on validation and test set are shown respectively:


| Task | Accuracy | Precision | Recall | F1     |
|------|----------|-----------|--------|--------|
| A    | 0.8340   | 0.7899    | 0.7255 | 0.7481 |
| B    | 0.5453   | 0.5258    | 0.4491 | 0.4675 |

| Task | Accuracy | Precision | Recall | F1       |
|------|----------|-----------|--------|----------|
| A    | 0.8405   | 0.7947  | 0.7444 | 0.0.7637 |
| B    | 0.5124   | 0.4932    | 0.4438 | 0.4597   |

The best SOTA results are related to the task A, while in the task B the results are not so promising due to the complexity of the problem.


## Evaluation Data 
### Details on the dataset(s) used for the quantitative analyses in the card.
- Datasets
- Motivation
- Preprocessing

## Training details
### Training Data 
### May not be possible to provide in practice. When possible, this section should mirror Evaluation Data. If such detail is not possible, minimal allowable information should be provided here, such as details of the distribution over various factors in the training datasets.

### Training Procedure
#### Preprocessing

#### Training hyperparameters



## Ethical Considerations

In this study ethical considerations were prioritized:
- avoid perpetuating stereotypes and worked towards fair and unbiased representation in the detection and categorization of online sexism
- consider the ethical implications of deploying automated systems for sensitive tasks and advocate for ongoing discussions surrounding the ethical use of AI technologies

By addressing these ethical considerations, this project to contribute responsibly to the exploration of online sexism detection, recognizing the importance of maintaining integrity, fairness and respect for individuals throughout the research process.



## Caveats and Recommendations