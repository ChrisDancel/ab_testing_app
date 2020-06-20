# AB testing application

This application demonstrates how AB testing can work when comparing two distributions. 

#### Note
This is a one sided test with Distribution 2 > Distribution 1. 

#### Usage
* on the sidebar, change parameters to see how the distribution varies
* mean values for distribution 2 cannot be smaller than for distribution 1


# 1. Setup

### 1.1 Create new virtual environment
```mkvirtualenv ab_testing```

### 1.2 Install Packages
```pip3 install -r requirements.txt```

# 2. Run streamlit app locally
```streamlit run app.py```