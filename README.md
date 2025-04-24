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

The overall results - across all classes - were:
```json
{
  "accuracy": 0.5351013611153164,
  "macro avg": {"precision": 0.6253318711576416, "recall": 0.5988678181942607, "f1-score": 0.5348746482272928, "support": 72661.0},
  "weighted avg": {"precision": 0.7100654528964326, "recall": 0.5351013611153164, "f1-score": 0.49514278522591415, "support": 72661.0}
}
```

#### Experiment 2: Finetuning DistilBert

```
{'0': {'precision': 0.5365993634893306, 'recall': 0.8341443633414436, 'f1-score': 0.6530780709273899, 'support': 12330.0}, '1': {'precision': 0.39914453751559437, 'recall': 0.9112214175278704, 'f1-score': 0.5551259171128297, 'support': 12289.0}, '2': {'precision': 0.7224820010391153, 'recall': 0.9602446483180428, 'f1-score': 0.824565861922914, 'support': 10137.0}, '3': {'precision': 0.8757516802263884, 'recall': 0.26642453591606136, 'f1-score': 0.40855645859977724, 'support': 37170.0}, '4': {'precision': 0.051587301587301584, 'recall': 0.057777777777777775, 'f1-score': 0.05450733752620545, 'support': 225.0}, '5': {'precision': 0.9064039408866995, 'recall': 0.7215686274509804, 'f1-score': 0.8034934497816594, 'support': 510.0}, 'accuracy': 0.5711592188381662, 'macro avg': {'precision': 0.5819948041240716, 'recall': 0.6252302283886961, 'f1-score': 0.5498878493117959, 'support': 72661.0}, 'weighted avg': {'precision': 0.7138729239153097, 'recall': 0.5711592188381662, 'f1-score': 0.5345523531018376, 'support': 72661.0}}

```
