import pandas as pd
import plotly.graph_objects as go

# Load the Excel file
file_path = '../Jesse - Job Applications 12_2023 - current.xlsx'
df = pd.read_excel(file_path, sheet_name='Sheet1')

# Define the states with separated Rejected and Ghosted
states = ["Applied", "Pre-screen", "1st Interview", "2nd Interview", "3rd Interview", "Rejected", "Ghosted"]
# Define the states with additional code test nodes
states = [
    "Applied",
    "Pre-screen",
    "Pre-Interview Code Test",
    "1st Interview",
    "Post Interview Code Test",
    "2nd Interview",
    "3rd Interview",
    "Rejected",
    "Ghosted"
]

# Initialize a dictionary to store the transitions
transitions = {state: {next_state: 0 for next_state in states} for state in states}
state_counts = {state: 0 for state in states}

# Populate the transitions dictionary and state counts
for i, row in df.iterrows():
    current_state = "Applied"
    state_counts[current_state] += 1
    
    if pd.notna(row['Pre-screen']):
        transitions[current_state]["Pre-screen"] += 1
        current_state = "Pre-screen"
        state_counts[current_state] += 1
    if pd.notna(row['Pre-Interview Code Test']):
        transitions[current_state]["Pre-Interview Code Test"] += 1
        current_state = "Pre-Interview Code Test"
        state_counts[current_state] += 1
    if pd.notna(row['1st Interview Date']):
        transitions[current_state]["1st Interview"] += 1
        current_state = "1st Interview"
        state_counts[current_state] += 1
    if pd.notna(row['Post Interview Code Test']):
        transitions[current_state]["Post Interview Code Test"] += 1
        current_state = "Post Interview Code Test"
        state_counts[current_state] += 1
    if pd.notna(row['2nd Interview']):
        transitions[current_state]["2nd Interview"] += 1
        current_state = "2nd Interview"
        state_counts[current_state] += 1
    if pd.notna(row['3rd Interview']):
        transitions[current_state]["3rd Interview"] += 1
        current_state = "3rd Interview"
        state_counts[current_state] += 1
    
    if pd.notna(row['Rejection Date']):
        transitions[current_state]["Rejected"] += 1
        state_counts["Rejected"] += 1
    else:
        transitions[current_state]["Ghosted"] += 1
        state_counts["Ghosted"] += 1

# Prepare data for Sankey diagram
source = []
target = []
value = []

for src in states:
    for tgt in states:
        if transitions[src][tgt] > 0:
            source.append(states.index(src))
            target.append(states.index(tgt))
            value.append(transitions[src][tgt])

# Update labels with counts
labels = [f"{state} ({state_counts[state]})" for state in states]

# Create Sankey diagram
fig = go.Figure(data=[go.Sankey(
    node=dict(
        pad=15,
        thickness=20,
        line=dict(color="black", width=0.5),
        label=labels,
    ),
    link=dict(
        source=source,
        target=target,
        value=value,
    ))])

# Save the figure as an HTML file
fig.write_html("job_application_process_sankey_updated.html")
