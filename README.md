Overview: 

This file contains information needed to run the submission for the Lumaa AI - AI/Machine Learning Intern Challenge. In this challenge, I have
made a simple content-based recommendation system that takes a short description of the user's preferences, and recommmends movies to the user.


1. The dataset comes from a public github repositorty training NLP techiniques on the plot summaries by Nazareno. If you run the code on github
   using Jupyter notebook, you should be able to run it with the csv file included in this repository. If you run it on Google Colab, you can simply
   add the dataset to files section in Google Colab or use files.upload to access it on your local computer or even get it from your google drive
   using drive.mount().


2. If you run this on google colab, the default python 3.10 works and all the necessary packages and libraries required to import is also provided
   at the top of the file. If you run this on Jupyter Notebook, you should have no issue simply running the latest python version in the kernel. If
   you use an older or different python version, you may have to change what you download from nltk, but Jupyter Notebook or Google Colab will tell
   what different library version you need from nltk. 


3. With the uploaded ipynb file added to this repository, you can run the code in Jupyter notebook. I created the code on Google Colab,
   but with the ipynb gile, it should work fine on either platform. You can see the demo in the repository on how the code would run in
   Google Colab.

4. A sample query that I ran had a user input of "I like drama films with romance in them." with a defined term of n = 3 for the top 3
recommendations. The result or output of this sample query was

              title
     1.Network
     2.Singin' in the Rain
     3.The Grapes of Wrath
