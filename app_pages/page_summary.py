import streamlit as st
import matplotlib.pyplot as plt


def page_summary_body():

    st.write("### Quick Project Summary")

    st.info(
        f"**General Information**\n"
        f"* Powdery mildew, a fungal infection sometimes affecting cherry trees, is transmitted via airborne spores. "
        f"Effective control measures often include cultural practices, such as pruning to enhance air circulation, "
        f"and the application of fungicides. Additionally, selecting cherry varieties resistant to powdery mildew can aid in prevention."
    )

    st.warning(
        f"**Cherry Leaves Dataset**\n\n"
        f"\n The dataset is obtained from [Kaggle](https://www.kaggle.com/codeinstitute/cherry-leaves).\n"
        f"With an even distribution, the dataset comprises 2104 healthy leaves and 2104 leaves affected by powdery mildew."
        f" The goal is to visually differentiate between the two categories of cherry leaves."
    )

    st.success(
        f"The project encompasses two key business requirements:\n"
        f"* 1 - Conduct a study to visually distinguish between infected and uninfected cherry leaves.\n"
        f"* 2 - Develop a model to determine whether a given leaf contains powdery mildew or not."
    )

    st.write(
        f"For further details, please visit and **read** the "
        f"[Project README file](https://github.com/Rackstorm/Code-Institute-Project-5).")
