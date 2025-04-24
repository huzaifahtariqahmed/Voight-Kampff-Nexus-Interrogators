import matplotlib.pyplot as plt
import ast

epochs = []
losses = []

with open("logs\subtask2\exp2_bertBase.txt", "r") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue  # skip empty lines
        try:
            data = ast.literal_eval(line)
            epochs.append(data['epoch'])
            losses.append(data['loss'])
        except Exception as e:
            print(f"Skipping line due to error: {line}\n{e}")

# Plot
plt.figure(figsize=(8, 5))
plt.plot(epochs, losses, marker='o', color='blue')
plt.title("Loss vs Epoch")
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.grid(True)
plt.tight_layout()
plt.show()
