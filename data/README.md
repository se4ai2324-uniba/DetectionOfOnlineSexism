# Dataset card
## Dataset Description

- title = SemEval-2023 Task 10: Explainable Detection of Online Sexism,
- url = http://arxiv.org/abs/2303.04222,
- doi = 10.48550/arXiv.2303.04222,
- author = Kirk, Hannah Rose and Yin, Wenjie and Vidgen, Bertie and Röttger, Paul,
- booktitle = Proceedings of the 17th International Workshop on Semantic Evaluation (SemEval-2023),
- publisher = Association for Computational Linguistics,
- year = 2023

## Dataset Summary
Online sexism is a widespread and harmful phenomenon. To address this issue "SemEval Task 10 on the Explainable Detection of Online Sexism" (EDOS) has been introduced. 
Have been done two main contributions:
- a novel hierarchical taxonomy of sexist content, which includes granular vectors of sexism to aid explainability; 

- a new dataset of 20,000 social media comments with fine-grained labels, along with larger unlabelled datasets for model adaptation.

## Languages
This task supports the development of English-language models for sexism detection that are more accurate as well as explainable.

# Dataset Structure
## Data Instances
The dataset has two columns: 
- `rewire_id`: is the unique ID of each entry, as specified in the dev/test data;
- `label_pred`: is the string label predicted by your model for each entry. The label names must exactly match those from the training data.

For Task A, label_pred must be one of two labels:
- `not sexist`;
- `sexist`.

For Task B, label_pred must be one of four labels:

1. `threats, plans to harm and incitement`;
2. `derogation`;
3. `animosity`;
4. `prejudiced discussions`.

## Data Splits

The dataset has been splitted into validation, test and training set.
The class distribution for
Task A was as follows:
- TRAIN SET:
    - not sexist: 10602
    - sexist: 3398
- DEV SET:
    - not sexist: 1514
    - sexist: 486
- TEST SET:
    - not sexist: 3030
    - sexist: 970

As regards task B, the class distribution was:
- TRAIN SET:
    - derogation: 1590
    - animosity: 1165
    - prejudiced discussions: 333
    - threats, plans to harm and incitement:310
- DEV SET:
    - derogation: 227
    - animosity: 167
    - prejudiced discussions: 48
    - threats, plans to harm and incitement: 44
- TEST SET:
    - derogation: 454
    - animosity: 333
    - prejudiced discussions: 94
    - threats, plans to harm and incitement: 89

