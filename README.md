# **🎮 Video Game Sales Analysis**
![Alt text](/Images/image.png)

## Contents

Project Checkpoints
[README](/README.md)
[Project Board](https://github.com/users/MichaelJDB/projects/5/views/1)
[Raw Data](/Data/vgsales.csv)
[Clean Data](/Data/vgsales_cleaned.csv)
[Data Cleaning](/jupyter_notebooks/DataCleaning.ipynb)
[EDA](/jupyter_notebooks/EDA.ipynb)
[Machine Learning](/jupyter_notebooks/MachineLearning.ipynb)
[Streamlit](/Streamlit/dashboard.py)
[Streamlit images](/Streamlit/DBIMG.png)

## **Project Overview**

This project focuses on Video Game Sales (1980-2011), looking at the range of factors that effect the market and supporting companies with their future decisions with the content they create by looking at successes from previous data.

## **Datasent Content**

The Video Game Sales dataset I used came from Kaggle: https://www.kaggle.com/datasets/thedevastator/global-video-game-sales-and-reviews/data

| Field Name       | Description |
|------------------|-------------|
| index            | Row index or unique identifier for each entry |
| Rank             | Ranking position of the game based on global metrics |
| Game Title       | Title of the video game |
| Platform         | Gaming platform (e.g., PS4, Xbox, PC) |
| Year             | Release year of the game |
| Genre            | Game genre (e.g., Action, RPG, Sports) |
| Publisher        | Company that published the game |
| North America    | Sales or popularity score in North America |
| Europe           | Sales or popularity score in Europe |
| Japan            | Sales or popularity score in Japan |
| Rest of World    | Sales or popularity score in other regions |
| Global           | Total global sales or popularity score |
| Review           | Review score or rating of the game |

## **Business Requirements**

As I chose my own dataset there was no business requirements that came with it. I will make my own business requirement in this schenario. A business requires the development of an interactive analytics dashboard that leverages the video game sales dataset, which contains information on game titles, platforms, release years, genres, publishers, regional sales (North America, Europe, Japan, Rest of World), global sales, and review scores. The dashboard must enable product managers and marketing analysts to filter and visualise sales performance across regions, identify top-performing genres and platforms over time, and evaluate publisher success by global reach and best-selling titles. By providing clear insights into historical sales trends and regional preferences, the tool will support strategic decision-making for future game launches, targeted marketing campaigns, and portfolio optimisation, ensuring that resources are invested in the most profitable genres, platforms, and regions.

## **Hypothesis Testing and Validation**

**Hypothesis 1:** Sports games generate the highest global sales among all genres.

**Conclusion** The bar chart confirms that sports games lead in global sales, followed by Action and Platform genres. However, Role-Playing games claim high review scores but rank fith in sales. This shows that theres a potential gap between critical acclaim and commercial success which suggests that mass market appeal is providing a drive in revenue.

![alt text](/Images/output1.png)

**Hypothesis 2:** Role-Playing games recieve higher average review scores than other genres.

**Conclusion** The bar chart proves that role-playing games constitently gain the highest average review scores, showing strong critical acclaim. Genres like strategy and fighting also perform well with reviews compared to miscellaneous titles that lack. This implies that the complexity of games may correclate with better reception.

![alt text](/Images/output2.png)

**Hypothesis 3:** North America contributes the largest share of global video game sales compared to other regions.

**Conclusion** The treemap confirms that North America dominates global video game sales, it claims over 50% of the total volumes. Europe follows as a distant second, while Japan and the rest of the world trail significantly behind. This suggests that companies show create marketing strategies and game development towards North American consumers while also studying trends to improve the market for other regions.

![alt text](/Images/output3.png)

**Hypothesis 4:** Sales distribution vary widely across platforms, with some showing extreme outliers.

**Conclusion:** The box plot reveals significant variability in plaform performance, with the Wii showing the highest outlier (80 million units). Platforms like NES, GB, and PS2 also show strong medians and wide ranges. This suggests that while some platforms have consistent sales, others rely heavily on popular game titles to drive sales.

![alt text](/Images/output4.png)

**Hypothesis 5:** The PS2 is the most successful gaming platform in terms of total global sales.

**Conclusion:** The horizontal bar chart confirms that PS2 leads all plaforms in total global sales which is then followed by Wii and the Xbox 360. Legacy platforms like the NES and GB still hold strong positions, while handhelds like the GBA round up the list. This shows the enduring impact of early console generations and the importance of plaform life.

![alt text](/Images/output5.png)

## *Project Plan**

![alt text](/Images/ProjectBoard.png)

### *Steps Taken** 

The analysis had followed a structured approach: 

**1. Data Collection** - The dataset was sourced from Kaggle and made into the CSV format.
**2. Data Cleaning and Processing** - Steps taken in this were checking data types, locating missing values, checking for duplicates.
**3. Exploratory Data Analysis(EDA)** - Descriptive and reasonable statistics.
**4. Data Storage & Exportation** - The cleaned dataset was saved as (/Data/vgsales_cleaned.csv).
**5. Analyis & Interpretation** - A variation of data was analysed using a range of charts and machine learning to answer hypotheses and predict future statistics.

## **Analysis Techniques Used:**

The analysis combined descriptive statistics, data visualisation, and exploratory data analysis (EDA).

**Descriptive statistics** (mean, median, counts) were used to summarize sales across genres, platforms, and regions.

|**Data visualiwation** with Altair, Matplotlib, Seaborn, and Plotly provided interactive charts to reveal trends over time and highlight top publishers.

**Correlation analysis** was applied to explore relationships between review scores and sales.

**Machine learning models** (e.g., scikit‑learn regression) were tested to predict sales based on features like genre, platform, and critic scores.

### **Limitations:**

* Sales data is historical and may not reflect current market dynamics.

* Missing or inconsistent values (e.g., publisher names, regional sales) reduced model accuracy.

* Regression models struggled with categorical variables like genre, platform, global without careful encoding and time.

## **Use of Generative AI Tools**

**Ideation:** Brainstorming ideas with charts and dashboarding - to support and develop further on my original ideas(hypotheses)
**Troubleshooting:** Fix or find work around errors especially with my Streamlit deployment.
**General Queries:** Answer or provide support for small tasks that I didn't know or forgot parts of.
**Visualisation** Improving and helping with code for my dashboarding and machine learning.

## **Ethical Considerations** 

**Data Completeness and Representation:** The dataset may overrepresent certain regions (North America, Europe) while also underrepresenting others (Japan, Rest of the World). This creates a risk of bias is conclusions become generalised. 

**Genre and Platform Categorisation:** Broad categories like "Action" "Puzzle" may cover up suber-genre diversity leading to simplified oversights. 

**Temporal Bias:** Older game titles may lack complete sales or review data which brings focus to more recent releases.

**Publisher Dominance:** Large publishers with more titles will appear more successful than more recent ones.

**Ethical Use of Insights:** Stakeholders must avoid misuising the dashboard to justify exclusions of genres or regions, which can take an effect on diversity in the gaming industry.

### **How To Mitigate These**

* Normalise sales by region to compare popularity rather than raw totals.
* Aggregating data into broader time ranges to smooth gaps and reduce noise.
* Using visulisation to highlight diversity instead of relying on predictive models.
* Ensure the use of the dashboard is appropiate. 

## **Unfixed Bugs**

I was having issues with the deployment of my Streamlit which took a huge toll on my time with the rest of the project's progress. The deployment of the dashboard either needs fixing or another app will need to be created for the dashboarding like Tableu or Heroku but these will have to be completed in the future due to the deadline.

## **Libraries Used**

| Library            | Purpose                                                                 |
|--------------------|-------------------------------------------------------------------------|
| **numpy**          | Numerical computing, arrays, and mathematical operations                |
| **pandas**         | Data manipulation and analysis                                          |
| **matplotlib**     | Static plotting and visualization                                      |
| **seaborn**        | Statistical data visualization built on matplotlib                     |
| **plotly**         | Interactive charts and dashboards                                      |
| **streamlit**      | Framework for building interactive data apps and dashboards            |
| **altair**         | Declarative statistical visualization library                          |
| **feature-engine** | Feature engineering tools for machine learning                         |
| **imbalanced-learn** | Handling imbalanced datasets in machine learning                      |
| **scikit-learn**   | Machine learning algorithms and preprocessing                          |
| **xgboost**        | Gradient boosting machine learning library                             |
| **ydata-profiling** | Automated exploratory data analysis (profiling reports)                |
| **ppscore**        | Predictive power score for feature relevance                           |
| **yellowbrick**    | Machine learning visualization toolkit                                 |
| **Pillow**         | Image processing library                                               |

## **Credits**

* The Code Institute LMS which provided me with the knowledge in order to use to the libraries and sources in this project as well as being a resource for checking my work.
* Microsoft Copilot which has supported me with my visuals and troubleshooting errors I have encountered throuhgout the project especially my dashboarding and deployment.
* Kaggle which I had resourced my dataset from to create my project.
* I used previous projects supplied by my coach to inspire my project layout.

## **Acknowledgments**

* Special Thanks to my work coaches: Emma Lamont, Mark Briscoe, Neil, and my previous coach Spencer Barriball for all the support, knowledge and encouragement they have given me!
