This version uses D3 to generate the Sankey Diagram.

There is a bug in `convert.js`, so the numbers are wrong.

Also, yes, I could ask ChatGPT to put `convert.js` into `server.js`.

# Prompt

I used `ChatGPT 4o` to generate this in the same conversation as I generated the python version.

## Turn 1

> Can you also do this in d3.js?

## Turn 2

> Use Node-xlsx to read the xlsx and output the necessary data to JSON. Then read the JSON from the d3 HTML page.

## Turn 3

> My CORS policy is blocking me from reading sankey_data.json. Create a very basic express server to serve up sankey_data.json and index.html. Load d3 from node_modules. 


# Getting started

## Node

I'm using node `v20.11.1` installed via `nvm`.

## Install dependencies

```bash
npm install
```

## Convert spreadsheet data to JSON

```bash
node ./convert.js
```

## Run server

```bash
node server.js
```

## View

Browse to the `http://localhost:3000/` in your browser
