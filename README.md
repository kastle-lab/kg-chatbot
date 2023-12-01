# Video Game Chatbot

## Objective
This repository represents the work accomplished by me (Anmol Saini) under the supervision of Dr. Cogan Shimizu during an undergraduate honors independent study in the Spring and Fall 2023 semesters. The primary goal of this project is to develop a knowledge graph-powered agent (or chatbot) capable of multiturn conversations about video game information with users.

## Repository Structure
This section gives a brief overview of the layout of this repository.

- `resources`
  - `datasets`: Datasets used extensively for this project in some way
  - `scripts`
    - `kg`: Scripts related to creation of the knowledge graph using files in `mapping` and `/resources/datasets`
      - `mapping`: YAML files that delineate the relationships of the values in the rows of the CSVs in `/resources/datasets`
      - `kg_output_parser.py`: Script that takes TTL files generated by other scripts in `kg` and combines them into one TTL file
    - `web_scrape`: Scripts used to generate CSVs in `resources/datasets`
  - `conversational_scripts.md`: A file containing sample snippets modeling what conversations between the agent and a user could look like
  - `potential_datasets.md`: A list of datasets found online that could be useful for this project. Confirmed/Integrated datasets were moved into `resources/datasets`
- `schemas`
  - `convology_schema.graphml`: A schema of Convology I created using yEd and the documentation found [here](https://horus-ai.fbk.eu/convology/)
  - `convology.owl`: Convology's `owl` file downloaded from [here](https://horus-ai.fbk.eu/convology/)
  - `video_game_schema.graphml`: A schema I created for this project

## Methodology

what I think i'm doing for the departmental honors thesis (does not need to be perfect



what I've done and where I'm going
