# Emotion-Classification-Model

##DATASET USED

I have taken a dataset from kaggle. The dataset name is - "Emotions Dataset - Bhavik Jikadar".
Each entry in this dataset consists of a text segment representing a Twitter message and a corresponding label indicating the predominant emotion conveyed. The emotions are classified into six categories: sadness (0), joy (1), love (2), anger (3), fear (4), and surprise (5).
The dataset includes text samples with corresponding emotion labels.
text: Description of context
label: The emotions are classified into six categories: sadness (0), joy (1), love (2), anger (3), fear (4), and surprise (5).

## APPROACH SUMMARY

*Preprocessing:* Text data is cleaned and converted to lowercase.
*Feature Extraction:* TF-IDF Vectorizer is used to convert text into numerical features, removing                         English stop words and limiting to 5000 features.
*Model:* A Multinomial Naive Bayes classifier is trained on the TF-IDF vectors to predict emotion           classes.
*Evaluation:* The model is evaluated using accuracy score and a confusion matrix.
*Tes:* Test the model predictions manually by giving the data from test dataset.
*Demo:* Add a Gradio interface also that allows users to input text and get live emotion predictions.

## DEPENDENCIES

-Python 3.7 or higher
-pandas
-numpy
-matplotlib
-scikit-learn
-seaborn
-gradio

