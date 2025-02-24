# Movie Recommendation System

## Dataset
The dataset used in this project is obtained from Kaggle: "https://www.kaggle.com/datasets/rounakbanik/the-movies-dataset?select=movies_metadata.csv". It contains information about movies and their descriptions. 
The datset has been preprocessed, and the results are saved in movies.csv. The file includes only the top 500 movies, ensuring coverage across all genres. The final dataset retains only the following fields:

Title
Overview
Genre (processed as a list instead of JSON/dictionary)
Tagline

### Note:
If you want to perform the dataset filteration and processing steps, please download the movies_metadata.csv file from the link given above and run the dataset_preprocessing.py file using the command below. 
```bash
python dataset_processing.py 
```
However, this is not needed as I have already performed the process and saved the results in movies.csv which is added to this repo.

## Setup
### Requirements
- Python 3.8+
- Jupyter Notebook

### Installation
1. Clone this repository:
   ```bash
   git clone "https://github.com/shruthic06/lumaa-spring-2025-ai-ml"
   cd lumaa-spring-2025-ai-ml
   ```
2. Create a virtual environment (Recommended):
   ```bash
   python3 -m venv <path-to-lumaa-spring-2025-ai-ml>
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. Install dependencies: 
   ```bash
   pip3 install -r requirements.txt
   ```

## Running the Code
To run the code, open Jupyter Notebook by the command jupyter notebook in the terminal and open the file movie_recommendation.ipynb and click on run all.

To run the code from command terminal, I have converted the ipynb file to py file so you can directly run it there:
```bash
python movie_recommendation.py 
```
The user will be prompted with - "What kind of movie are you looking for? ". Give your input here.
Next there is another prompt - "Do you want to read the plots of these movies as well? (yes/no): "

## Sample Results
For example, if the input is:
```bash
"A science fiction movie with aliens"
```

```bash
"Yes"
```

The output would be:

```
Here are the top 5 movies recommended for you:
Childhood's End
Parasyte: Part 1
Parasyte: Part 2
Independents' Day
Alive in Joburg
```
Do you want to read the plots of these movies as well? (yes/no): yes

Movie: Childhood's End
Plot: After peaceful aliens invade earth, humanity finds itself living in a utopia under the indirect rule of the aliens, but does this utopia come at a price?


Movie: Parasyte: Part 1
Plot: Alien pods come to Earth and, naturally, start taking over Human Hosts. One such pod only manages to take over one human's, Shin Izumi, right arm. Together they grow and co-exist, all the while the other aliens are making meals of other humans; Shin feels he must put a stop to it all, but his alien, Migi, doesn't see why.


Movie: Parasyte: Part 2
Plot: Alien pods come to Earth and, naturally, start taking over Human Hosts. One such pod only manages to take over one human's, Shin Izumi, right arm. Together they grow and co-exist, all the while the other aliens are making meals of other humans; Shin feels he must put a stop to it all, but his alien, Migi, doesn't see why.


Movie: Independents' Day
Plot: Aliens invade, this time delivering a clear ultimatum. The fate of humanity hangs in the balance as the U.S. President and citizens decide if these aliens are to be trusted ...or feared.


Movie: Alive in Joburg
Plot: A documentary-style short film about the arrival of an alien spaceship over Johannesburg, South Africa.


**[Click Here to Watch the Demo](https://drive.google.com/drive/folders/1o4hYsuO6sq6LqEK9hMQXlw8bW-GoSwNw?usp=sharing)**


## Notes
- Ensure `movies.csv` is present in the same directory as the script.
