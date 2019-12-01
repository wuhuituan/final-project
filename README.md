# final-project
Data scrape and visualization

Introduction

Python's position in data science is not only because of numpy, scipy, pandas, scikit-learn, which are efficient and easy to use, and the interface is unified scientific computing package. Its powerful data visualization tool is also an important part. 
In Python, the most used data visualization tool is matplotlib, in addition to many other optional visualization toolkits, including the following major categories:

1 Matplotlib and toolkit based on matplotlib: the drawing function of the matplotlib API in pandas, seaborn, networkx, etc;

2 Visualization tools based on JavaScript and d3.js: plotly, etc. These tools can display dynamic graphs with certain interactivity;

3 Other visualization tools that provide Python call interfaces: OpenGL, GraphViz, etc. These tools have their own characteristics.

In this project, I want to scrape the data form webpage(weather.com) and make the data visulizabable.
Follow are overall thought process:

1 Get the response information of the page to be scraped through the URL (using the Requests library).

2 Structured parsing of the response through the parsing library in python (use of the BeautifulSoup library).

3 Organize data into a certain format for storage (use of Pandas library).

4 Filter and organize the data in the database for the initial display of data visualization (use of Matplotlib library).

In code part,we use python to scrape data form weather.com,specificlly 10 days forecast.Then we organize data and show 
them in a figure.


