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

#### Experiment 2: Finetuning BertBaseUncased

```
{'0': {'precision': 0.5377620221948212, 'recall': 0.8489051094890511, 'f1-score': 0.6584261181354972, 'support': 12330.0}, '1': {'precision': 0.4214704732107939, 'recall': 0.8769631377654813, 'f1-score': 0.5693230143426926, 'support': 12289.0}, '2': {'precision': 0.6798832235725439, 'recall': 0.9878662326131992, 'f1-score': 0.805437143086946, 'support': 10137.0}, '3': {'precision': 0.8819901315789473, 'recall': 0.2885391444713479, 'f1-score': 0.43482667747820797, 'support': 37170.0}, '4': {'precision': 0.052478134110787174, 'recall': 0.08, 'f1-score': 0.06338028169014084, 'support': 225.0}, '5': {'precision': 0.9696202531645569, 'recall': 0.7509803921568627, 'f1-score': 0.8464088397790055, 'support': 510.0}, 'accuracy': 0.5833115426432336, 'macro avg': {'precision': 0.5905340396387417, 'recall': 0.6388756694159904, 'f1-score': 0.5629670124187484, 'support': 72661.0}, 'weighted avg': {'precision': 0.715540932775255, 'recall': 0.5833115426432336, 'f1-score': 0.548959655838386, 'support': 72661.0}}

```

#### Data Augmentation

```
{'0': {'precision': 0.47640257344670894, 'recall': 0.8587996755879967, 'f1-score': 0.6128425499898718, 'support': 12330.0}, '1': {'precision': 0.482186344367277, 'recall': 0.8700463829440963, 'f1-score': 0.6204915416533674, 'support': 12289.0}, '2': {'precision': 0.6858394960284854, 'recall': 0.9880635296438789, 'f1-score': 0.8096681621599774, 'support': 10137.0}, '3': {'precision': 0.887276958882855, 'recall': 0.3076943771859026, 'f1-score': 0.45693168198162204, 'support': 37170.0}, '4': {'precision': 0.27009646302250806, 'recall': 0.37333333333333335, 'f1-score': 0.31343283582089554, 'support': 225.0}, '5': {'precision': 0.9956043956043956, 'recall': 0.888235294117647, 'f1-score': 0.938860103626943, 'support': 510.0}, 'accuracy': 0.5955189166127633, 'macro avg': {'precision': 0.6329010385587049, 'recall': 0.7143620988021425, 'f1-score': 0.6253711458721128, 'support': 72661.0}, 'weighted avg': {'precision': 0.7197891743216054, 'recall': 0.5955189166127633, 'f1-score': 0.5631998873774842, 'support': 72661.0}}
