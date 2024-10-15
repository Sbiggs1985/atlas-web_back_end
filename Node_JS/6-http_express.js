const express = require('express');
const app = express();

// Define the endpoint for "/"
app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});

// Start the server and listen on port 1245
app.listen(1245, () => {
  console.log('Server running on http://localhost:1245/');
});

// Export the app module
module.exports = app;