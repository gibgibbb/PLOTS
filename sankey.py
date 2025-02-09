import pandas as pd
import plotly.graph_objects as go

DATASET_PATH = './csv/'
IMAGE_PATH = './img/'

sankey_df = pd.read_csv(DATASET_PATH + "sankey_assignment.csv")

def find_distance_sankey(mid, target):
    return sankey_df.loc[sankey_df['LABEL'] == mid, target].values[0]

start = list(sankey_df.columns[1:9])
middle = list(sankey_df['LABEL'].unique())

end = list(sankey_df.columns[9:])

node_labels = start + middle + end

node_indices = {x: i for i, x in enumerate(node_labels)}

source = []
target = []
value = []

for s in start:
    for m in middle:
        dist = find_distance_sankey(m, s)
        if dist > 0:
            source.append(node_indices[s])
            target.append(node_indices[m])
            value.append(dist)
            
for e in end:
    for m in middle:
        dist = find_distance_sankey(m, e)
        if dist > 0:
            source.append(node_indices[m])
            target.append(node_indices[e])
            value.append(dist)

colors = [
    '#FFA07A',  # PS
    '#20B2AA',  # OMP
    '#FF8C00',  # CNP
    '#FF6AB4',  # NRP
    '#8FBC8F',  # NMCCC
    '#02CED1',  # PEC
    '#FFD701',  # NCDM
    '#BA55D3',  # RGS
    '#87CEFA',  # S
    '#4782B4',  # F
    '#5F9EA0',  # D
    '#6395EC',  # N 
    '#00BFFF',  # I
    '#3CB371',  # Reg
    '#97FB98',  # Aca
    '#90EE8F'   # Oth
]

fig = go.Figure(data=[go.Sankey(
    node=dict(
        pad=15,
        thickness=20,
        line=dict(color="black", width=0.5),
        label=node_labels,
        color=colors
    ),
    link=dict(
        source=source,
        target=target,
        value=value,
        color=[colors[s] for s in source]
    )
)])

fig.update_layout(title_text="Sankey Diagram: Source → Intermediate → Target", font_size=10)

# Save the figure as a PNG
# fig.write_image(IMAGE_PATH + "sankey_diagram.png")

# Show the plot
fig.show()