# Video Game Recommendation System

This project is a **content-based recommendation system** for video games. Given a video game as input, the system recommends similar games based on features such as platform, genre, critic scores, user scores, global sales, and rating.

## Features

- **Input**: A video game title (e.g., "Grand Theft Auto V").
- **Output**: A list of similar video games ranked by similarity score.
- **Similarity Calculation**: Uses **cosine similarity** to measure similarity between games based on their features.

## Dataset

The dataset used for calculation includes the following columns:

- `Name`: Name of the game.
- `Platform`: Gaming platform (e.g., PC, Xbox, PlayStation).
- `Genre`: Genre of the game (e.g., Action, RPG, Shooter).
- `Critic_Score`: Average critic review score.
- `User_Score`: Average user review score.
- `Global_Sales`: Total global sales (in millions).
- `Rating`: ESRB rating (e.g., T, E, M).

## How It Works

1. **Data Preprocessing**:
   - Categorical features (`Platform`, `Genre`, `Rating`) are **one-hot encoded**.
   - Numerical features (`Critic_Score`, `User_Score`, `Global_Sales`) are **normalized**.

2. **Cosine Similarity**:
   - A similarity matrix is calculated using cosine similarity on the preprocessed feature matrix.
   - The system retrieves the most similar games based on the similarity scores.

3. **Recommendations**:
   - Given an input game name, the system outputs the top `N` most similar games.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/KhuongBao/lumaa-spring-2025-ai-ml.git
    cd video-game-recommendation
    ```

2. Install the required Python libraries:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

### Running the Jupyter Notebook

1. Open **main.ipynb** in Jupyter Notebook or any IDE
2. Run all cells to train and use the recommendation system.

### Example

Input:

```bash
Enter a game name: Grand Theft Auto V
```

### Video Demo: [LINK](https://youtu.be/7MPFRs_u1pM)
