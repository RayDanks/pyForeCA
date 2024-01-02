# pyForeCA
A Python implementation of Forecastable Component Analysis (ForeCA).

This Python implementation is aided by [the R implementation of ForeCA](https://cran.r-project.org/web/packages/ForeCA/vignettes/Introduction.html), and the accompanying [GitHub repository.](https://github.com/gmgeorg/ForeCA)

For a full explanation on the ForeCA algorithm, see the original paper: \
**Goerg, G. (2013). Forecastable Component Analysis. In S. Dasgupta & D. McAllester (Eds.), Proceedings of the 30th International Conference on Machine Learning (Vol. 28, Issue 2, pp. 64–72). PMLR. https://proceedings.mlr.press/v28/goerg13.html**

# Usage
Import The package after installing it to your pip or conda environment
```
import pyforeca
```

Instantiate a ForeCA object
```
foreca_obj = pyforeca.ForeCA()
```

Use this object to run analysis on your chosen series
```
output = foreca_obj.run(series)
```
Your series is expected to be a multivariate time series. If the number of components (n_comp) is not passed to the object, then it is inferred from the series. Currently Pandas DataFrames and Numpy Arrays are supported as multivariate inputs.

The output is in the form of a Pandas DataFrame with all relevant results and components.

## Input Parameters
Below we outline an exhaustive list of all possible input parameters, as well as their default values:




