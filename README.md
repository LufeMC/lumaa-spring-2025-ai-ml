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
   python -m venv <path-to-lumaa-spring-2025-ai-ml>
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. Install dependencies: 
   ```bash
   pip install -r requirements.txt
   ```

## Running the Code
To run the code, open Jupyter Notebook and open the file movie_recommendation.ipynb and execute the cells step by step.

To run the code from command terminal, I have converted the ipynb file to py file so you can directly run it there:
```bash
python movie_recommendation.py 
```
The user will be prompted with - "What kind of movie are you looking for? ". Give your input here.
Next there is another prompt - "Do you want to read the plots of these movies as well? (yes/no): "

## Sample Results
For example, if the input is:
```bash
"A science fiction movie with space adventure"
```

```bash
"Yes"
```

The output would be:

```
Here are the top 5 movies recommended for you:
Battleship
Ender's Game
Independence Day: Resurgence
The 5th Wave
Edge of Tomorrow
```
Do you want to read the plots of these movies as well? (yes/no): yes

Movie: Battleship
Plot: When mankind beams a radio signal into space, a reply comes from ‘Planet G’, in the form of several alien crafts that splash down in the waters off Hawaii. Lieutenant Alex Hopper is a weapons officer assigned to the USS John Paul Jones, part of an international naval coalition which becomes the world's last hope for survival as they engage the hostile alien force of unimaginable strength. While taking on the invaders, Hopper must also try to live up to the potential his brother, and his fiancée's father, Admiral Shane, expect of him.


Movie: Ender's Game
Plot: Based on the classic novel by Orson Scott Card, Ender's Game is the story of the Earth's most gifted children training to defend their homeplanet in the space wars of the future.


Movie: Independence Day: Resurgence
Plot: We always knew they were coming back. Using recovered alien technology, the nations of Earth have collaborated on an immense defense program to protect the planet. But nothing can prepare us for the aliens’ advanced and unprecedented force. Only the ingenuity of a few brave men and women can bring our world back from the brink of extinction.


Movie: The 5th Wave
Plot: 16-year-old Cassie Sullivan tries to survive in a world devastated by the waves of an alien invasion that has already decimated the population and knocked mankind back to the Stone Age.


Movie: Edge of Tomorrow
Plot: Major Bill Cage is an officer who has never seen a day of combat when he is unceremoniously demoted and dropped into combat. Cage is killed within minutes, managing to take an alpha alien down with him. He awakens back at the beginning of the same day and is forced to fight and die again... and again - as physical contact with the alien has thrown him into a time loop.


## Notes
- Ensure `movies.csv` is present in the same directory as the script.
