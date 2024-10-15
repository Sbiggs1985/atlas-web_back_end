const http = require('http');
const countStudents = require('./3-read_file_async');
const url = require('url');

const app = http.createServer(async (req, res) => {
  const parsedUrl = url.parse(req.url, true);

  if (parsedUrl.pathname === '/') {
    res.writeHead(200, { 'Content-Type': 'text/plain' });
    res.write('Hello Holberton School!');
    res.end();
  } else if (parsedUrl.pathname === '/students') {
    res.writeHead(200, { 'Content-Type': 'text/plain' });
    res.write('This is the list of our students\n');

    // Pass the database file as a command-line argument
    const database = process.argv[2];

    try {
      const result = await countStudents(database);
      res.write(result); // Write the student list to the response
    } catch (error) {
      res.write(error.message); // Handle errors (e.g., file not found)
    }

    res.end();
  } else {
    res.writeHead(404, { 'Content-Type': 'text/plain' });
    res.write('Not Found');
    res.end();
  }
});

app.listen(1245);

module.exports = app;
