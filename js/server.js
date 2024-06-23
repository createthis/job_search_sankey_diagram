const express = require('express');
const path = require('path');

const app = express();
const port = 3000;

// Serve static files from the root directory
app.use(express.static(path.join(__dirname)));

// Route for the main page
app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'index.html'));
});

// Route for the JSON data
app.get('/sankey_data.json', (req, res) => {
    res.sendFile(path.join(__dirname, 'sankey_data.json'));
});

app.listen(port, () => {
    console.log(`Server is running at http://localhost:${port}`);
});
