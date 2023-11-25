import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.image import imread
from src.machine_learning.evaluate_clf import load_test_evaluation


def page_ml_performance_metrics():
    version = 'v1'

    st.write("### Train, Validation and Test Set: Labels Frequencies")

    st.info(
        f'The dataset for this project is sourced from [Kaggle](https://www.kaggle.com/codeinstitute/cherry-leaves).\n'
        f'It includes images of 2104 healthy leaves and 2104 infected leaves. '
        f'The dataset is divided into three sets for training, validation, and test.'
    )

    labels_distribution = plt.imread(
        f"outputs/{version}/labels_distribution.png")
    st.image(labels_distribution,
             caption='Labels Distribution on Train, Validation and Test Sets')

    st.write("### Model History")

    st.info(
        f'The graphs illustrate the ML model learning cycle, showcasing '
        f'accuracy and loss during training. The model follows a '
        f'typical learning curve, indicating no overfitting or underfitting.')

    col1, col2 = st.beta_columns(2)
    with col1:
        model_acc = plt.imread(f"outputs/{version}/model_training_acc.png")
        st.image(model_acc, caption='Model Training Accuracy')
    with col2:
        model_loss = plt.imread(f"outputs/{version}/model_training_losses.png")
        st.image(model_loss, caption='Model Training Losses')

    st.write("### Generalised Performance on Test Set")
    st.dataframe(pd.DataFrame(load_test_evaluation(
        version), index=['Loss', 'Accuracy']))
