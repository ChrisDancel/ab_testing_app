import pandas as pd
import numpy as np

import streamlit as st
import altair as alt
import matplotlib.pyplot as plt
from scipy.stats import norm


def get_stats_ab_test(mean_1, std_1, mean_2, std_2):
    z_score = (mean_2 - mean_1) / np.sqrt(std_1**2 + std_2**2)

    p_value = norm.sf(z_score)
    ci = norm.cdf(z_score)
    return z_score, p_value, ci


markdown_text = """
This application demonstrates how AB testing can work when comparing two distributions. 

Note - this is a one sided test with Distribution 2 > Distribution 1

#### Usage
* on the sidebar, change parameters to see how the distribution varies
* mean values for distribution 2 cannot be smaller than for distribution 1


"""


def main():
    st.write('# AB Test Demo - 1 sided')
    st.markdown(markdown_text)

    # create parameter selections in slider
    st.sidebar.markdown('# Parameter Selection')
    alpha = st.sidebar.slider('alpha', value=0.05, step=0.01)
    mean_1 = st.sidebar.slider('Mean of Distribution 1', value=10.0, step=0.1, min_value=0.0, max_value=20.0)
    std_1 = st.sidebar.slider('Standard Deviation of Distribution 1', value=0.1, step=0.02, min_value=0.02, max_value=2.0)
    size_1 = st.sidebar.slider('# Samples in Distribution 1', value=1000, min_value=100, max_value=10000)

    mean_2 = st.sidebar.slider('Mean of Distribution 2', value=mean_1 + 1, step=0.1, min_value=mean_1, max_value=mean_1 + 3)
    std_2 = st.sidebar.slider('Standard Deviation of Distribution 2', value=0.1, step=0.02, min_value=0.02, max_value=2.0)
    size_2 = st.sidebar.slider('# Samples in Distribution 2', value=1000, min_value=100, max_value=10000)

    s1 = np.random.normal(mean_1, std_1, size_1)
    s2 = np.random.normal(mean_2, std_2, size_2)

    # compute distribution stats
    z_score, p_value, ci = get_stats_ab_test(mean_1, std_1, mean_2, std_2) 

    # calculate if the two distributions are signifcantly different
    if p_value <= alpha:
        sig = True
        st.write('### Evaluation: Significant Difference found :)')
    else:
        sig = False
        st.write('### Evaluation: Not Significant Difference found :(', )

    plot_params = {'bins': 50, 'alpha': 0.7}
    plt.hist(s1, color='b', **plot_params);
    plt.hist(s2, color='r', **plot_params);
    plt.legend(['Dist. 1','Dist. 2']);
    plt.xlabel('Value'); plt.ylabel('Count');
    plt.title('p-value {:.4f}, z score {:.2f}'.format(p_value, z_score))
    st.pyplot()
    
    st.write("""
    Dist 2 > Dist 1 {:.2f}% of the time, equivalent to 1 - p_value or 1 - {:.4f}
    """.format((1-p_value)*100, p_value))

    
if __name__ == '__main__':
    main()
