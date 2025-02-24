# Movie Recommendation System

This project is a content-based recommendation system that suggests movies based on a user's input query.

## Dataset

- The dataset contains movie descriptions.
- It is stored as a CSV file (`movies.csv`).
- It is automatically loaded when running the script.

## Setup

### 1. Clone the Repository

```bash
git clone https://github.com/vivek-krishnagiri/lumaa-spring-2025-ai-ml.git
cd lumaa-spring-2025-ai-ml
```

### 2. Create and Activate a Virtual Environment

#### macOS/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

#### Windows (CMD)

```bash
python -m venv venv
venv\Scripts\activate
```

#### Windows (PowerShell)

```powershell
python -m venv venv
venv\Scripts\Activate.ps1
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

## Running the Recommendation System

Run the following command with a search query to get relevant movie recommendations:

```bash
python recommend.py "sci-fi movies with space battles"
```

### Example Queries

```bash
python recommend.py "romantic movies with tragic endings"
python recommend.py "animated movies about talking animals"
python recommend.py "mystery movies with mind-blowing twists"
python recommend.py "action movies with intense fight scenes"
```

## Example Output

For the query **"sci-fi movies with space battles"**, the output may look like:

```
1. Guardians of the Galaxy - A group of misfits fights in space to save the universe.
2. Interstellar - A team of explorers travel through a wormhole to find a new home for humanity.
3. Star Wars - A young Jedi learns the ways of the Force and battles the dark side.
4. The Matrix - A hacker discovers reality is a simulation and fights back.
5. Gravity - A medical engineer and an astronaut work together to survive in space.
```
## demo.md file is uploaded to the Github

## 8000 per month salary requested
