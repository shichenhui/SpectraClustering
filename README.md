# Data mining techniques on astronomical spectra data.I Clustering analysis
This is the experiment code of the paper - [https://doi.org/10.1093/mnras/stac2975](https://doi.org/10.1093/mnras/stac2975).

Through the experiments, we found that GMM performs better than others on 1D spectra and PCA features, and on stellar spectra line indices, GMM performs the same as partition-based methods. Spectra line indices can extract stellar spectra features effectively, and the clustering results of many methods on them is better than 1D spectra. Density-based algorithms and hierarchical clustering perform poorly on spectral related datasets, although they have many advantages on benchmark datasets. The reason is that, in spectra dataset, there is no clear separation between different types of spectra, and the density distribution maybe different, so it is impossible to find appropriate parameters for effective clustering.

Although in supervised classification algorithm, overfitting can be reduced when the size of dataset is larger, but in clustering, the amount of data has little influence on the clustering results, and some algorithms can not be run when the amount of data is too large. Although GMM has a good effect on spectra data, its running time is much higher than other methods when there is a large amount of data. K-means is still a good choice if you want to make a fast clustering of data.

The experiments also showed that clustering methods are very effective to find abnormal spectra. Multiple cluster centers can be found first, and then the samples far from the cluster center can be regarded as outliers, and this method is also very robust. When researchers want to observe the distribution of spectra data, the visualization methods of dimensionality reduction are very intuitive, like t-SNE, UMAP and SOM, and SOM is widely used in astronomy to find special spectra.

## Bib cite

@article{10.1093/mnras/stac2975,
    author = {Yang, Haifeng and Shi, Chenhui and Cai, Jianghui and Zhou, Lichan and Yang, Yuqing and Zhao, Xujun and He, Yanting and Hao, Jing},
    title = "{Data mining techniques on astronomical spectra data – I. Clustering analysis}",
    journal = {Monthly Notices of the Royal Astronomical Society},
    volume = {517},
    number = {4},
    pages = {5496-5523},
    year = {2022},
    month = {09},
    issn = {0035-8711},
    doi = {10.1093/mnras/stac2975},
    url = {https://doi.org/10.1093/mnras/stac2975},
    eprint = {https://academic.oup.com/mnras/article-pdf/517/4/5496/46951728/stac2975.pdf},
}
