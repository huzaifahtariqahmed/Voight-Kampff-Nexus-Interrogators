# Voight-Kampff Generative AI Detection 2025 
## PAN LAB - CLEF 2025
## Team: Nexus Interrogators

## Sub-Task 1 - Voight-Kampff AI Detection Sensitivity

Given a (potentially obfuscated) text, decide whether it was written by a human or an AI.

## Sub-Task 2 - Human-AI Collaborative Text Classification

Given a document collaboratively authored by human and AI, classify the extent to which the model assisted.


## Results

### Sub-Task 2

#### Experiment 1: Finetuning Sentimental Analysis Model.

| Metric    | Class 0            | Class 1            |  Class 2           | Class 3            | Class 4            | Class 5            |
|-----------|--------------------|--------------------|--------------------|--------------------|--------------------|--------------------|
| precision | 0.5134855337002125 | 0.3481732397774014 | 0.8322803980960624 | 0.8617745596022911 | 0.3333333333333333 | 0.8629441624365483 |
| recall    | 0.7643146796431468 | 0.9367727235739279 | 0.948702772023281  | 0.2145278450363196 | 0.06222222222222222| 0.6666666666666666 |
| f1-score  | 0.6142815239709285 | 0.5076621171697573 | 0.8866863359763968 | 0.3435366090084656 | 0.10486891385767791| 0.7522123893805309 | 
| support   | 12330.0            | 12289.0            | 10137.0            | 37170.0            | 225.0              | 510.0              |
