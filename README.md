# Voight-Kampff Generative AI Detection 2025 
## PAN LAB - CLEF 2025
## Team: Nexus Interrogators

## Sub-Task 1 - Voight-Kampff AI Detection Sensitivity

It is a binary AI detection task in that participants are given a text and have to decide whether it was machine-authored (class 1) or human-authored (class 0). However, we introduced a twist: The LLMs were instructed to change their style and mimic a specific human author. Furthermore, the test set will contain several surprises such as new models or unknown obfuscations to test the robustness of the classifiers (however, texts will be from the same domain).

## Sub-Task 2 - Human-AI Collaborative Text Classification

Here the goal is to categorize documents that have been co-authored by humans and LLMs. Specifically, we aim to classify texts into six distinct categories based on the nature of human and machine contributions:

- Fully human-written: The document is entirely authored by a human without any AI assistance.
- Human-initiated, then machine-continued: A human starts writing, and an AI model completes the text.
- Human-written, then machine-polished: The text is initially written by a human but later refined or edited by an AI model.
- Machine-written, then machine-humanized (obfuscated): An AI generates the text, which is later modified to obscure its machine origin.
- Machine-written, then human-edited: The content is generated by an AI but subsequently edited or refined by a human.
- Deeply-mixed text: The document contains interwoven sections written by both humans and AI, without a clear separation.
- Accurately distinguishing between these categories will enhance our understanding of human-AI collaboration and help mitigate the risks associated with synthetic text.
