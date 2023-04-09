# Video Game Chatbot

## Objective
This repository represents the work accomplished by me (Anmol Saini) under the supervision of Dr. Cogan Shimizu during an undergraduate honors independent study in the Spring and Fall 2023 semesters. The primary goal of this project is to develop a knowledge-graph-powered agent (or chatbot) capable of multiturn conversations about video game information with users.

## Repository Structure
This section gives a brief overview of the layout of this repository.

- `resources`
  - `datasets`
    - `artist-dataset.csv`: A dataset containing game names and illustrators
    - `music-dataset.csv`: A dataset containing game names, album names, track names, and composer names
    - `va-dataset.csv`: A dataset containing game names, character names, and voice actor names
  - `scripts`
    - `artist-scrape.py`: A script used to generate [`resources/datasets/artist-dataset.csv`](https://github.com/kastle-lab/kg-chatbot/blob/readme-init/resources/scripts/artist-scrape.py)
    - `music-scrape.py`: A script used to generate [`resources/datasets/music-dataset.csv`](https://github.com/kastle-lab/kg-chatbot/blob/readme-init/resources/datasets/music-dataset.csv)
    - `va-scrape.py`: A script used to generate [`resources/datasets/va-dataset.csv`](https://github.com/kastle-lab/kg-chatbot/blob/readme-init/resources/datasets/va-dataset.csv)
  - `conversational-scripts.md`: A file containing sample snippets modeling what conversations between the agent and a user could look like
  - `potential-datasets.md`: A list of datasets found online that could be useful for this project. Confirmed/Integrated datasets will be moved into `resources/datasets`
- `schemas`
  - `Convology-Schema.graphml`: A schema of Convology I created using yEd and the documentation found [here](https://horus-ai.fbk.eu/convology/)
  - `convology.owl`: Convology's `owl` file downloaded from [here](https://horus-ai.fbk.eu/convology/)

## Methodology
