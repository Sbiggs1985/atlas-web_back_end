const http = require('http');
const countStudents = require('./3-read_file_async'); // Import the function

const app = http.createServer((req, res) => {
  if (req.url === '/') {
    res.writeHead(200, { 'Content-Type': 'text/plain' });
    res.write('Hello Holberton School!');
    res.end();
  } else if (req.url === '/students') {
    countStudents('database.csv')
      .then((data) => {
        res.writeHead(200, { 'Content-Type': 'text/plain' });
        res.write(`This is the list of our students ${data}`);
        res.end();
      })
      .catch(() => {
        res.writeHead(500, { 'Content-Type': 'text/plain' });
        res.write('Cannot load the database');
        res.end();
      });
  }
});

app.listen(1245, () => {
  console.log('Server running at http://localhost:1245/');
});
