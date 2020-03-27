from bokeh.models import Div

#header
header = Div(text="""<h1>SPINNED SENTENCES CLUSTERING</h1>""")

# title for the toolbox
toolbox_header = Div(text="""<h1>Toolbox:</h1>""")

# project description
description = Div(text="""<p1>Given a large amount of spinned sentences regarding the rapidly spreading <b>web</b>, 
it is difficult for a SEO to keep up with the Google Search updates promptly. <u>Can we cluster similar spinned sentences 
together to make it easier for SEO professionals to find dissimilar sentences?</u> Clustering can be used to create 
a tool to identify similar sentences, given a spin. It can also reduce the number of sentences one has to go through as 
one can focus on a cluster of sentences rather than many different kinds. On this plot, we demonstrate how clustering can 
be used to achieve this.</p1>""")

# steps description
description2 = Div(text="""<h3>Approach:</h3><p1>This scatter plot is generated using <b>NLP parsed text</b> from the body of 
each spinned sentence as a feature. Then each instance is turned into features vector using Sklearn's <b>TfidfVectorizer</b>. 
Then, <b>Dimensionality Reduction</b> is applied to the feature vectors using Sklearn's <b>t-SNE</b>. Finally, labels are 
generated with the means of clustering using Sklearn's <b>k-Means</b> where k=20. <b>Topic Modeling</b> is done on each cluster
to get the keywords per cluster. <b>spaCy</b> is used to tokenize each instance first. Then, Sklearn's <b>CountVectorizer</b> is used to vectorize the features. Finally, Sklearn's <b>LatentDirichletAllocation</b> trained to get the keywords. Total of <b>18,000 samples</b> analysed.</p1>""")

# citation
cite = Div(text="""<p1><h3>Citation:</h3></p1>""")

description_search = Div(text="""<h3>Filter by Text:</h3><p1>Search keyword to filter out the plot. It will search the spinned sentences. Press enter when ready. 
Clear and press enter to reset the plot.</p1>""")

description_slider = Div(text="""<h3>Filter by the Clusters:</h3><p1>The slider below can be used to filter the target cluster. 
Simply slide the slider to the desired cluster number to display the plots that belong to that cluster. 
Slide back to 20 to show all.</p1>""")


notes = Div(text="""<h3>Contact:</h3>""")

dataset_description = Div(text="""<h3>Dataset Description:</h3><p1><i>'In response to the Google Search updates, 
a very smart SEO and a coalition of leading SEO groups have prepared the 18k spins test dataset.""")



