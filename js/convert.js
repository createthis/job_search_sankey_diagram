const xlsx = require('node-xlsx').default;
const fs = require('fs');

// Read the Excel file
const workSheetsFromFile = xlsx.parse(`${__dirname}/../Jesse - Job Applications 12_2023 - current.xlsx`);
const data = workSheetsFromFile[0].data;

// Define the states
const states = ["Applied", "Pre-screen", "1st Interview", "2nd Interview", "3rd Interview", "Rejected", "Ghosted"];

// Initialize a dictionary to store the transitions and state counts
let transitions = {};
let stateCounts = {};

states.forEach(state => {
    transitions[state] = {};
    states.forEach(nextState => {
        transitions[state][nextState] = 0;
    });
    stateCounts[state] = 0;
});

// Populate the transitions dictionary and state counts
data.slice(1).forEach(row => {
    let currentState = "Applied";
    stateCounts[currentState] += 1;
    
    if (row[4]) {
        transitions[currentState]["Pre-screen"] += 1;
        currentState = "Pre-screen";
        stateCounts[currentState] += 1;
    }
    if (row[7]) {
        transitions[currentState]["1st Interview"] += 1;
        currentState = "1st Interview";
        stateCounts[currentState] += 1;
    }
    if (row[11]) {
        transitions[currentState]["2nd Interview"] += 1;
        currentState = "2nd Interview";
        stateCounts[currentState] += 1;
    }
    if (row[13]) {
        transitions[currentState]["3rd Interview"] += 1;
        currentState = "3rd Interview";
        stateCounts[currentState] += 1;
    }
    
    if (row[15]) {
        transitions[currentState]["Rejected"] += 1;
        stateCounts["Rejected"] += 1;
    } else {
        transitions[currentState]["Ghosted"] += 1;
        stateCounts["Ghosted"] += 1;
    }
});

// Prepare the JSON data for the Sankey diagram
let nodes = states.map(state => ({ name: `${state} (${stateCounts[state]})` }));
let links = [];

states.forEach((src, i) => {
    states.forEach((tgt, j) => {
        if (transitions[src][tgt] > 0) {
            links.push({
                source: i,
                target: j,
                value: transitions[src][tgt]
            });
        }
    });
});

// Write the JSON data to a file
fs.writeFileSync(`${__dirname}/sankey_data.json`, JSON.stringify({ nodes, links }, null, 2));
