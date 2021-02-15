# MALIS-project

This project was made by two Telecom Paris and Eurecom students, who started studying Machine Learning and Intelligent Systemes (MALIS). 

The aim of this project is to have a first manipulation of the technics and algorithms of machine learning.

We decided to work on the RSI indicator, which is a financial stock market indicator. It allows a trader to follow and try to predict the trend of a stock. 
Indeed, the RSI uses two parameters (the upper one and the lower one), and when the RSI signal is over the upper parameter it means that the asset is overbougth and a drop can be expected. Accordingly when the RSI signal is below the lower parameter it means that the asset is oversold and an increase of the asset value can be expected.

However, we thought that those two parameters could be optimized for a given market situation.

As a result, we decided to define a market situation by 19 different asset such as Gold, Oil, Dollar Index, Nasdaq, and many more.
Then we created a dataset composed of the best market situation for all differrent couple of parameters.

Once we had this dataset we decided to train a neural network. 

When the neural network was trained, it was capable for a given market situation to return the optimal couple of parameters for the RSI.
