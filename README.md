![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

## Codeanywhere Template Instructions

Welcome,

This is the Code Institute student template for Codeanywhere. We have preinstalled all of the tools you need to get started. It's perfectly ok to use this template as the basis for your project submissions. Click the `Use this template` button above to get started.

You can safely delete the Codeanywhere Template Instructions section of this README.md file, and modify the remaining paragraphs for your own project. Please do read the Codeanywhere Template Instructions at least once, though! It contains some important information about the IDE and the extensions we use.

## How to use this repo

1. Use this template to create your GitHub project repo

1. Log into <a href="https://app.codeanywhere.com/" target="_blank" rel="noreferrer">CodeAnywhere</a> with your GitHub account.

1. On your Dashboard, click on the New Workspace button

1. Paste in the URL you copied from GitHub earlier

1. Click Create

1. Wait for the workspace to open. This can take a few minutes.

1. Open a new terminal and <code>pip3 install -r requirements.txt</code>

1. In the terminal type <code>pip3 install jupyter</code>

1. In the terminal type <code>jupyter notebook --NotebookApp.token='' --NotebookApp.password=''</code> to start the jupyter server.

1. Open port 8888 preview or browser

1. Open the jupyter_notebooks directory in the jupyter webpage that has opened and click on the notebook you want to open.

1. Click the button Not Trusted and choose Trust.

Note that the kernel says Python 3. It inherits from the workspace so it will be Python-3.8.12 as installed by our template. To confirm this you can use <code>! python --version</code> in a notebook code cell.

## Cloud IDE Reminders

To log into the Heroku toolbelt CLI:

1. Log in to your Heroku account and go to _Account Settings_ in the menu under your avatar.
2. Scroll down to the _API Key_ and click _Reveal_
3. Copy the key
4. In the terminal, run `heroku_config`
5. Paste in your API key when asked

You can now use the `heroku` CLI program - try running `heroku apps` to confirm it works. This API key is unique and private to you, so do not share it. If you accidentally make it public then you can create a new one with _Regenerate API Key_.

## Dataset Content

- The dataset is sourced from [Kaggle](https://www.kaggle.com/codeinstitute/cherry-leaves). We then created a fictitious user story where predictive analytics can be applied in a real project in the workplace.
- The dataset contains +4 thousand images taken from the client's crop fields. The images show healthy cherry leaves and cherry leaves that have powdery mildew, a fungal disease that affects many plant species. The cherry plantation crop is one of the finest products in their portfolio, and the company is concerned about supplying the market with a compromised quality product.

## Business Requirements

The cherry plantation crop from Farmy & Foods is facing a challenge where their cherry plantations have been presenting powdery mildew. Currently, the process is manual verification if a given cherry tree contains powdery mildew. An employee spends around 30 minutes in each tree, taking a few samples of tree leaves and verifying visually if the leaf tree is healthy or has powdery mildew. If there is powdery mildew, the employee applies a specific compound to kill the fungus. The time spent applying this compound is 1 minute. The company has thousands of cherry trees, located on multiple farms across the country. As a result, this manual process is not scalable due to the time spent in the manual process inspection.

To save time in this process, the IT team suggested an ML system that detects instantly, using a leaf tree image, if it is healthy or has powdery mildew. A similar manual process is in place for other crops for detecting pests, and if this initiative is successful, there is a realistic chance to replicate this project for all other crops. The dataset is a collection of cherry leaf images provided by Farmy & Foods, taken from their crops.

- 1 - The client is interested in conducting a study to visually differentiate a healthy cherry leaf from one with powdery mildew.
- 2 - The client is interested in predicting if a cherry leaf is healthy or contains powdery mildew.

## Hypothesis

We hypothesize that cherry leaves infected with powdery mildew exhibit noticeable visual contrasts when compared to healthy leaves. This distinction can potentially be captured through image analysis, allowing for the development of an effective machine learning model.

## How to Validate

To validate our hypothesis, we propose conducting an average image study using the dataset provided by Farmy & Foods. This study will involve a comprehensive analysis of cherry leaf images, aiming to identify distinctive visual patterns associated with powdery mildew infection. The outcome of this study will guide the development and training of a machine learning system capable of instantaneously detecting the presence of powdery mildew in cherry leaves. The success of the model will be measured against its accuracy in distinguishing between healthy and infected leaves, with the ultimate goal of streamlining the current manual verification process and providing a scalable solution for Farmy & Foods.

## The Rationale to Map Business Requirements to Data Visualizations and ML Tasks

### Business Requirements

#### Data Visualization

1. **Display "mean" and "standard deviation" images:**

   - **Rationale:** Provides a visual representation of the statistical measures for both mildewed and healthy cherry leaves, aiding in understanding the variation in pixel values and patterns.

2. **Display the difference between average mildewed and uninfected leaves:**

   - **Rationale:** Offers a visual comparison, allowing for a clear distinction between the characteristics of mildewed and healthy leaves, aiding in the identification of key features.

3. **Display an image montage for mildewed or uninfected leaves:**
   - **Rationale:** Creates a comprehensive visual overview, facilitating easy differentiation between mildewed and healthy cherry leaves in a montage format.

#### Classification

4. **Predict if a leaf is infected with powdery mildew:**

   - **Rationale:** Enables quick identification of infected leaves, contributing to efficient decision-making in cherry tree crop management.

5. **Build a binary classifier and generate reports:**
   - **Rationale:** Provides a structured approach to classification, with the added benefit of generating detailed reports for analysis and documentation.

### Data Visualization Tasks

- **Mean and Standard Deviation Visualization:**

  - **Objective:** Showcase statistical values for healthy and mildewed cherry leaf images.
  - **Benefit:** Enables clients to visually distinguish between the two types of leaves based on statistical measures.

- **Comparison Visualization:**

  - **Objective:** Illustrate distinctions between a typical healthy cherry leaf and one infected by powdery mildew.
  - **Benefit:** Provides a clear visual reference for differentiation, aiding in identification of key visual features.

- **Montage Visualization:**
  - **Objective:** Create a visual montage featuring both healthy and infected cherry leaves.
  - **Benefit:** Facilitates an overall understanding by presenting a comprehensive visual summary of the different leaf conditions.

### ML Classification Tasks

- **Prediction Capability:**

  - **Objective:** Develop a model to predict whether a given leaf is healthy or infected.
  - **Benefit:** Offers clients a quick and automated method for leaf classification.

- **Machine Learning Model App:**
  - **Objective:** Provide clients with an intuitive application for predicting leaf health.
  - **Benefit:** Enhances user experience by simplifying the prediction process through a user-friendly application.

By aligning these data visualization and machine learning tasks with the identified business requirements, we aim to deliver a solution that not only meets but exceeds the expectations of the client, providing valuable insights and efficient decision-making tools for managing cherry tree crops effectively.

## ML Business Case

### Overview:

- Development of MildewCherryLeavesCLF, a binary classification model.
- Goal: Predict presence of powdery mildew on cherry leaves.
- Revolutionize diagnostic process for Farmy & Foods' cherry tree crops.

### Objectives:

1. **Accuracy Target:**

   - Achieve 97% accuracy or above on the model's test set.

2. **Diagnostic Enhancement:**
   - Provide a faster and more reliable diagnostic tool.
   - Eliminate labor-intensive manual inspections (currently 30 minutes per tree).

### Model Details:

- **Model Type:**

  - Supervised, 2-class, single-label classification model.

- **Output:**

  - Binary flag: Infected or not.
  - Probability of infection.

- **Workflow:**
  - Botanical staff conduct visual inspections and upload leaf images to the app.
  - On-the-fly predictions enable real-time decision-making.

### Training Data:

- **Source:**

  - Subset of 2208 images from provided dataset.

- **Features:**

  - All images serve as features.

- **Target:**
  - Binary classification: Infected or not.

### Rationale:

- **Current Challenges:**
  - Manual inspection is time-consuming.
  - Prone to human error.
  - Specific facilities lack staff and expertise for effective fungal detection.

### Conclusion:

- MildewCherryLeavesCLF aims to enhance efficiency and accuracy in diagnosing powdery mildew. Streamlining diagnostics for Farmy & Foods and paving the way for scalable solutions across diverse crops.

## Dashboard Design

- List all dashboard pages and their content, either blocks of information or widgets, like buttons, checkboxes, images, or any other items, that your dashboard library supports.
- Finally, during the project development, you may revisit your dashboard plan to update a given feature (for example, at the beginning of the project, you were confident you would use a given plot to display an insight, but later, you chose another plot type).

## Unfixed Bugs

- You will need to mention unfixed bugs and why they were unfixed. This section should include shortcomings of the frameworks or technologies used. Although time can be a significant variable for consideration, paucity of time and difficulty understanding implementation is not a valid reason to leave bugs unfixed.

## Deployment

### Heroku

- The App live link is: https://YOUR_APP_NAME.herokuapp.com/
- Set the runtime.txt Python version to a [Heroku-20](https://devcenter.heroku.com/articles/python-support#supported-runtimes) stack currently supported version.
- The project was deployed to Heroku using the following steps.

1. Log in to Heroku and create an App
2. At the Deploy tab, select GitHub as the deployment method.
3. Select your repository name and click Search. Once it is found, click Connect.
4. Select the branch you want to deploy, then click Deploy Branch.
5. The deployment process should happen smoothly if all deployment files are fully functional. Click now the button Open App on the top of the page to access your App.
6. If the slug size is too large then add large files not required for the app to the .slugignore file.

### Languages

Python

### Frameworks and Other Technologies

- **Git:**

  - A distributed version control system that tracks changes in source code during software development.

- **GitHub:**

  - A web-based platform for version control using Git, facilitating collaborative software development and hosting repositories.

- **Heroku:**

  - A cloud platform that enables developers to deploy, manage, and scale applications effortlessly.

- **CodeAnywhere:**

  - An online development environment that allows coding from anywhere, offering collaboration features and support for multiple programming languages.

- **Jupyter:**
  - An open-source web application that allows the creation and sharing of live code, equations, visualizations, and narrative text in a single, interactive document.

## Main Data Analysis and Machine Learning Libraries

- **NumPy**

  - Efficient numerical operations and array manipulation in Python.

- **Pandas**

  - Data manipulation and analysis library, providing data structures for efficiently storing and manipulating large datasets.

- **Matplotlib**

  - Comprehensive 2D plotting library for creating static, animated, and interactive visualizations in Python.

- **Seaborn**

  - Statistical data visualization library based on matplotlib, providing an interface for creating informative and attractive statistical graphics.

- **Plotly**

  - Interactive graphing library for creating interactive, web-based visualizations.

- **Streamlit**

  - Open-source Python library for creating web applications with minimal effort, particularly well-suited for creating data dashboards.

- **Scikit**

  - Simple and efficient tools for data mining and data analysis, particularly for machine learning tasks.

- **Tensorflow**

  - Open-source machine learning library developed by the Google Brain team, used for building and training machine learning models.

- **Keras**

  - High-level neural networks API, written in Python and capable of running on top of TensorFlow, Theano, or Microsoft Cognitive Toolkit.

- **Protobuf**

  - Protocol Buffers, a method for serializing structured data, commonly used for communication between systems.

- **Altair**
  - Declarative statistical visualization library for Python, particularly well-suited for exploring and visualizing data.

## Credits

- [The Malaria Detector Walkthrough - Code Institute](https://learn.codeinstitute.net/courses/course-v1:code_institute+CI_DA_ML+2021_Q4/courseware/07a3964f7a72407ea3e073542a2955bd/29ae4b4c67ed45a8a97bb9f4dcfa714b/)
- [Mildew Detection by Albin Hall](https://github.com/AlbinHall/mildew-detection)
- [Mildew Detection by ssreelakshmi8](https://github.com/ssreelakshmi88/mildew-detection-cherry-leaves_milestonePP5)
- [Mildew Detection by olleholmgren 9](https://github.com/olleholmgren/mildew-detection)
- [Mildew Detection by Eric Jones](https://github.com/ericjonesdev/milestone-project-cherry-leaves-mildew-detection/)

### Content

- The text for the Home page was taken from Wikipedia Article A.
- Instructions on how to implement form validation on the Sign-Up page were taken from [Specific YouTube Tutorial](https://www.youtube.com/).
- The icons in the footer were taken from [Font Awesome](https://fontawesome.com/).

### Media

- The dataset is taken from [Kaggle](https://www.kaggle.com/datasets/codeinstitute/cherry-leaves/code)
- The template being used is generated from [Code Institute](https://github.com/Code-Institute-Solutions/milestone-project-mildew-detection-in-cherry-leaves)

## Acknowledgements (optional)

- All amazing students and mentors in the different Slack channels providing me with a lot of aha-moments throughout this journey.
