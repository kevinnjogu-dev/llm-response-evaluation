import json
import matplotlib.pyplot as plt


with open("data/evaluation_results.json", "r", encoding="utf-8") as file:
    data = json.load(file)


prompts = []
scores = []

for item in data:
    prompts.append(item["prompt"])
    scores.append(item["score"]["overall"])


plt.figure(figsize=(8, 5))

plt.bar(prompts, scores)

plt.ylabel("Overall Score")
plt.xlabel("Prompt")
plt.title("LLM Response Evaluation Scores")

plt.xticks(rotation=30, ha="right")

plt.tight_layout()

plt.savefig(
    "visualizations/score_distribution.png"
)

print("Visualization saved successfully.")