# Spinned Sentences Clustering

![](cover/interactive_plot.png)

### Goal
Given a large amount of *spinned sentences* and rapidly spreading *webs*, it is difficult for a *SEO* to keep up with the *text spins* promptly. Can we cluster *spinned sentences* to make it easier for *SEOs* to find *dissimilar* *spinned sentences*? Clustering can be used to create a tool to identify *dissimilar* *spins*, given a target *sentence*. It can also reduce the number of *spins* one has to go through as one can focus on a cluster of *spins* rather than all.

### [View the Interactive Spinned Sentences Clustering Plot]()
https://maksimekin.github.io/COVID19-Literature-Clustering/plots/t-sne_covid-19_interactive.html

![](plots/improved_cluster_tsne.png)
*t-SNE Output Clustered For Visualization*


**Approach**:
<ol>
    <li>Unsupervised Learning task, because we don't have labels for the articles</li>
    <li>Clustering and Dimensionality Reduction task </li>
    <li>See how well labels from K-Means classify</li>
    <li>Use N-Grams with Hash Vectorizer</li>
    <li>Use plain text with Tfidf</li>
    <li>Use K-Means for clustering</li>
    <li>Use t-SNE for dimensionality reduction</li>
    <li>Use PCA for dimensionality reduction</li>
    <li>There is no continuous flow of data, no need to adjust to changing data, and the data is small enough to fit in memmory: Batch Learning</li>
    <li>Altough, there is no continuous flow of data, our approach has to be scalable as there will be more literature later</li>
</ol>
<br>

### Dataset Description

>*In response to the Google Search updates, 
a very smart SEO and a coalition of leading SEO groups have prepared the 18k spins test dataset.*

