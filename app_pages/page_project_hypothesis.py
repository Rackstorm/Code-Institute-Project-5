import streamlit as st
import matplotlib.pyplot as plt


def page_project_hypothesis_body():
    st.write("### Project Hypothesis and Validation")

    st.info(
        f"* We hypothesize that mildewed cherry leaves display distinct marks, "
        f"such as leaf discoloration and markings, enabling differentiation from uninfected leaves.\n"
        f"* An Image Montage typically reveals powdery mildew on an infected leaf.\n "
        f"* Average Image, Variability Image, and the Difference between Averages "
        f"are utilized to distinguish between healthy and infected leaves.\n"
        f"* We posit that these features are sufficient for discerning a healthy leaf from an infected leaf.\n"
        f"* The ML model is expected to achieve a minimum accuracy of 70% in distinguishing "
        f"between a healthy cherry leaf and an infected cherry leaf.\n"
    )

    st.success(
        f"* We assert that cherry leaves infected with "
        f"powdery mildew exhibit distinct differences in color and appearance compared to purely green, "
        f"healthy cherry leaves, making the distinctions visibly apparent.\n"

        f"* An Image Montage illustrates the evident differences "
        f"between the two types of leaves, with powdery mildew appearing white and discolored, "
        f"while healthy cherry leaves maintain their normal green coloring.\n"

        f"* Average Image, Variability Image, and the Difference "
        f"confirm our hypothesis, showing color differences between healthy and infected leaves, "
        f"though no clear identifiers were found via leaf shape.\n"

        f"* The ML pipeline's performance was evaluated, and it successfully differentiates "
        f"between a healthy leaf and an infected leaf "
        f"with a minimum accuracy of 97%.\n\n"
    )
