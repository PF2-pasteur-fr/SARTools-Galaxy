-----------------------------------------------------------
sartools_1_1_0: a galaxy wrapper for SARTools version 1.1.0
-----------------------------------------------------------

Description:
------------
    SARTools is a R package dedicated to the differential analysis of RNA-seq data.
    
    SARTools provides tools to generate descriptive and diagnostic graphs, to run the differential analysis with one of the well known DESeq2 or edgeR packages and to export the results into easily readable tab-delimited files. It also facilitates the generation of a HTML report which displays all the figures produced, explains the statistical methods and gives the results of the differential analysis. Note that SARTools does not intend to replace DESeq2 or edgeR: it simply provides an environment to go with them. For more details about the methodology behind DESeq2 or edgeR, the user should read their documentations and papers.

Requirements:
-------------
    R (3.1.0 or higher), Bio-conductor package 
    SARTools package (1.1.0)
    other R packages: DESeq2 (1.6.0 or higher), edgeR (3.8.5 or higher), genefilter, xtable and knitr
    Rscript

    SARTools 1.1.0 can be downloaded on github (https://github.com/PF2-pasteur-fr/SARTools). More information about installation can be found at this url.

Requirements using Conda:
-------------------------
[![install with bioconda](https://img.shields.io/badge/install%20with-bioconda-brightgreen.svg?style=flat)](http://bioconda.github.io/recipes/r-sartools/README.html)

[Conda](http://conda.pydata.org/) is package manager that among many other things can be used to manage Python packages.


```
#To install miniconda2
#http://conda.pydata.org/miniconda.html
#To install the SARTools R library using conda:
conda install r-sartools
#To set an environment:
conda create -n r-sartools r-sartools`
#To activate the environment:
. activate r-sartools
```


Test:
-----

`planemo test` using conda: passed 


References:
-----------
    The SARTools package has been developped at PF2 - Institut Pasteur by M.-A. Dillies and H. Varet (hugo.varet@pasteur.fr). 
    Thanks to cite H. Varet, J.-Y. Coppee and M.-A. Dillies, SARTools: a DESeq2- and edgeR-based R pipeline for comprehensive differential analysis of RNA-seq data, 2015 (submitted) when using this tool for any analysis published. 

    The Galaxy wrapper and scripts have been developped by Loraine Brillet-Guéguen, Institut Français de Bioinformatique

