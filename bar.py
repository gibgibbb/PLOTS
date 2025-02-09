import pandas as pd
import matplotlib.pyplot as plt
import os

# -------------------------------
# Step 1: Load the Data
# -------------------------------
# Make sure the CSV file is in the same folder as your script or provide the full path.
DATASET_PATH = './csv/'
bar_df = pd.read_csv(DATASET_PATH + "bar_assignment.csv")

# -------------------------------
# Step 2: Transform the Data
# -------------------------------
# Convert the binary COUNT values to "Yes" and "No"
bar_df["COUNT"] = bar_df["COUNT"].map({1: "Yes", 0: "No"})

# Group by 'LABEL' and the transformed 'COUNT', then count the occurrences
# The unstack method pivots the 'COUNT' values into separate columns (i.e., Yes and No)
bar_counts = bar_df.groupby(["LABEL", "COUNT"]).size().unstack(fill_value=0)

# -------------------------------
# Step 3: Set Up Consistent Font Settings
# -------------------------------
# Set a common font family and font size for all text in the plots
plt.rcParams["font.family"] = "Arial"
plt.rcParams["font.size"] = 12

# -------------------------------
# Step 4: Create the Horizontal Stacked Bar Chart
# -------------------------------
fig, ax = plt.subplots(figsize=(10, 6))

# Plot the horizontal stacked bar chart
# The 'color' parameter sets the color for each stacked part. Here, we assume:
# "No" (0) will be red and "Yes" (1) will be blue.
bar_counts.plot(kind="barh", stacked=True, ax=ax, color=["red", "blue"])

# Customize axes labels and title
ax.set_xlabel("Y-LABELS", fontsize=12)
ax.set_ylabel("X-LABELS", fontsize=12)
ax.set_title("Bar Chart LABEL VS COUNT", fontsize=14)

# Customize legend: Note that the order of labels should match the order of columns in bar_counts.
# In our grouping, "No" comes before "Yes" alphabetically.
ax.legend(title="Response", labels=["No", "Yes"], fontsize=12, title_fontsize=12)

# Optionally add value labels inside each bar segment
for container in ax.containers:
    ax.bar_label(container, label_type="center", fontsize=10, color="white")

# Adjust layout to ensure everything fits without overlapping
plt.tight_layout()

# Display the plot
plt.show()