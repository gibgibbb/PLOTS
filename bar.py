import pandas as pd
import matplotlib.pyplot as plt

DATASET_PATH = './csv/'
bar_df = pd.read_csv(DATASET_PATH + "bar_assignment.csv")

bar_df["COUNT"] = bar_df["COUNT"].map({1: "Yes", 0: "No"})

bar_counts = bar_df.groupby(["LABEL", "COUNT"]).size().unstack(fill_value=0)


plt.rcParams["font.family"] = "Arial"
plt.rcParams["font.size"] = 12

fig, ax = plt.subplots(figsize=(10, 6))


bar_counts.plot(kind="barh", stacked=True, ax=ax, color=["red", "blue"])

ax.set_xlabel("Y-LABELS", fontsize=12)
ax.set_ylabel("X-LABELS", fontsize=12)
ax.set_title("Bar Chart LABEL VS COUNT", fontsize=14)


ax.legend(title="Response", labels=["No", "Yes"], fontsize=12, title_fontsize=12)

for container in ax.containers:
    ax.bar_label(container, label_type="center", fontsize=10, color="white")

plt.tight_layout()

plt.show()