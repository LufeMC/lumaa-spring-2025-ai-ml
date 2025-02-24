# AI/Machine Learning Intern Challenge: Simple Content-Based Recommendation

**Deadline**: Sunday, Feb 23th 11:59 pm PST

---

## Overview

This system generates personalized movie recommendations based on user input. It works by first processing the user’s query and identifying relevant genres from it. The movie dataset is then filtered based on the detected genres to narrow down the options.

To rank the movies, the system calculates similarity scores between the user query and movie descriptions, ensuring the recommendations are closely related to the user’s interests. Additionally, a genre match score is incorporated to further prioritize movies that align with the user’s genre preferences.

If the user specifies a preferred country, the system filters the recommendations to give higher priority to movies from that country. Finally, the system combines the similarity and genre match scores into a weighted score, which is used to rank the movies and return the top recommendations.

This approach combines both content-based filtering and genre-based preferences, providing diverse and relevant movie suggestions based on the user’s input.

---
## Video Link
1. Link = "https://drive.google.com/file/d/1B5FkmcRccOCfWZmTi-xb26oD-JoURVQ7/view?usp=sharing"
   
---

## Requirements

1. **Dataset**  
   - Download the **titles.csv** in the repository
     
2. **Setup**:
   - Python version, virtual environment instructions, and how to install dependencies (`pip install -r requirements.txt`).  
3. **Running**: Run the **main.ipynb** notebook
4.    **Results**: 
        User query: "I love space action movies"<br>
       📌 Detected Genres: ['action']<br>

       🔍 Top 10 Recommendations:
       
       1. 🎬 A StoryBots Space Adventure<br>
             📖 Join the StoryBots and the space travelers of the historic Inspiration4 mission as they search for answers to kids' questions about space.<br>
             🌎 []<br>
             🎭 Genres: animation<br>
       --------------------------------------------------
       2. 🎬 The Wonderful: Stories from the Space Station<br>
             📖 In unusual circumstances, scientists from different countries work together to achieve a common scientific goal. Locked in their spinning space lab, they are isolated from the world — family and friends - and can only watch from the outside as life on Earth continues without them. The space station is a monument not only to the weaknesses of humanity, but also to its ability to do the impossible for the sake of life in space.<br>
             🌎 ['US']<br>
             🎭 Genres: documentation<br>
       --------------------------------------------------
       3. 🎬 Fukrey Boyzzz: Space Mein Fukrapanti<br>
             📖 Delhi Boys Going To Space<br>
             🌎 []<br>
             🎭 Genres: animation, comedy, family<br>
       --------------------------------------------------
       4. 🎬 Action Pack<br>
             📖 The heroic kids of the Action Academy take on the bad guys with their hearts, their wits and their superpowers, and bring out the best in them.<br>
             🌎 ['US']<br>
             🎭 Genres: family, action, animation, fantasy, scifi, comedy<br>
       --------------------------------------------------
       5. 🎬 Space Force<br>
             📖 A four-star general begrudgingly teams up with an eccentric scientist to get the U.S. military's newest agency — Space Force — ready for lift-off.<br>
             🌎 ['US']<br>
             🎭 Genres: comedy<br>
       --------------------------------------------------
       6. 🎬 Last Action Hero<br>
             📖 Following the death of his father, young Danny Madigan takes comfort in watching action movies featuring the indestructible Los Angeles cop Jack Slater. After being given a magic ticket by theater manager Nick, Danny is sucked into the screen and bonds with Slater. When evil fictional villain Benedict gets his hands on the ticket and enters the real world, Danny and Jack must follow and stop him.<br>
             🌎 ['US']<br>
             🎭 Genres: action, fantasy, comedy, family<br>
       --------------------------------------------------
       7. 🎬 Space Sweepers<br>
             📖 When the crew of a space junk collector ship called The Victory discovers a humanoid robot named Dorothy that's known to be a weapon of mass destruction, they get involved in a risky business deal which puts their lives at stake.<br>
             🌎 ['KR']<br>
             🎭 Genres: scifi, drama, fantasy, action<br>
       --------------------------------------------------
       8. 🎬 The Space Between Us<br>
             📖 In this interplanetary adventure, a space shuttle embarks on the first mission to colonize Mars, only to discover after takeoff that one of the astronauts is pregnant. Shortly after landing, she dies from complications while giving birth to the first human born on the red planet – never revealing who the father is. Thus begins the extraordinary life of Gardner Elliot – an inquisitive, highly intelligent boy who reaches the age of 16 having only met 14 people in his very unconventional upbringing.<br>
             🌎 ['CN', 'US']<br>
             🎭 Genres: drama, romance, action, scifi<br>
       --------------------------------------------------
       9. 🎬 Tito<br>
             📖 Tito is the second installment in the new-wave Egyptian action movies. After Mafia by Sherif Arafa, which was a breakthrough in Egyptian cinema making, Tarek El-Aryan brings us Tito, the next logical step. Very simply, this movie is about an ex-con who tries to escape his sinful life by starting a new one, but his past comes back to haunt him. The reason, why Tito is better than Mafia is because the script and story line in Tito is more complex, and some of the characters had real depth in them and where fully developed throughout the movie.<br>
             🌎 ['EG']<br>
             🎭 Genres: documentation, crime, drama, romance, action<br>
       --------------------------------------------------
       10. 🎬 The Getaway King<br>
             📖 An action crime comedy set in the last days of communism in Poland, a story of folk-hero thief, who escaped 29 times from cops. Naymro was living on his own terms against the system. But love and collapsing Berlin Wall changed everything.<br>
             🌎 ['PL']<br>
             🎭 Genres: drama, action, comedy, crime<br>

---
**Salary Expectations** - 3000- 5000
