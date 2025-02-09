import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np


DATASET_PATH = './csv/'
IMAGE_PATH = './img/'

# Load the dataset
networks_df = pd.read_csv(DATASET_PATH + "networks_assignment.csv")

# Define the function to find distances
def find_distance_networks(source, target):
    return networks_df.loc[networks_df['LABELS'] == source, target].values[0]

# Define the function to find edges
def find_edges(collection, source, target):
    for s in source:
        for t in target:
            dist = find_distance_networks(s, t)
            if dist > 0:
                collection.append((s, t))

# Define node categories
blue_nodes = ['D', 'F', 'I', 'N', 'S']
green_nodes = ['BIH', 'GEO', 'ISR', 'MNE', 'SRB', 'CHE', 'TUR', 'UKR', 'GBR', 'AUS', 'HKG', 'ASU']
yellow_nodes = ['AUT', 'BEL', 'BGR', 'HRV', 'CZE', 'EST', 'FRA', 'DEU', 'GRC', 'HUN', 'IRL', 'ITA', 
                'LVA', 'LUX', 'NLD', 'PRT', 'ROU', 'SVK', 'SVN', 'ESP']

nodes = blue_nodes + green_nodes + yellow_nodes

# Initialize edge lists
bb_edges = []
bg_edges = []
by_edges = []

# Find Edges
find_edges(bb_edges, blue_nodes, blue_nodes)
find_edges(bg_edges, blue_nodes, green_nodes)
find_edges(by_edges, blue_nodes, yellow_nodes)

edges = bb_edges + bg_edges + by_edges

# Create the graph
G = nx.Graph()
G.add_nodes_from(nodes)
G.add_edges_from(edges)

# Define positions
pos = nx.circular_layout(G.subgraph(green_nodes + yellow_nodes), center=(0, 0), scale=1.0)
pos.update({
    'D': np.array([0, 0.5]),
    'F': np.array([0.35, 0.15]),
    'I': np.array([-0.35, 0.15]),
    'N': np.array([-0.20, -0.4]),
    'S': np.array([0.20, -0.4])
})

# Define colors for nodes
color_set = [
    (node_set, color) for node_set, color in zip(
        map(set, [blue_nodes, green_nodes, yellow_nodes]), 
        ['#0197B2', '#00C063', '#FFDE59']
    )
]

colors = [
    color for (node_set, color) in color_set for node in nodes if node in node_set 
]

# Draw the graph
plt.figure(figsize=(10, 8))
nx.draw_networkx_nodes(G, pos, node_color=colors, node_size=700)
nx.draw_networkx_labels(G, pos, font_weight='bold', font_size=8, font_color='white')
nx.draw_networkx_edges(G, pos, arrows=False, edge_color='black')

# Save image to IMAGE_PATH (uncomment to save)
plt.savefig(IMAGE_PATH + 'network_graph.png')

plt.title("Network Graph")
plt.show()
