const express = require('express');

const app = express();

app.get('/', (req, res) => {
    res.send('Hello Holberton School!');
});

// Set the app to listen on port 1245
app.listen(1245, () => {
    console.log('Server is listening on port 1245');
});

module.exports = app;