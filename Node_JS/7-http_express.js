const express = require('express');
const fs = require('fs');
const app = express();
const port = 1245;

// Helper function to count students and categorize by field
const countStudents = (database) => {
  return new Promise((resolve, reject) => {
    fs.readFile(database, 'utf-8', (err, data) => {
      if (err) {
        reject(new Error('Cannot load the database'));
      } else {
        const lines = data.split('\n').filter((line) => line.trim() !== ''); // Ignore empty lines
        const fields = {};
        let totalStudents = 0;

        lines.slice(1).forEach((line) => { // Ignore the header
          const studentData = line.split(',');
          if (studentData.length === 4) {
            const field = studentData[3].trim();
            const name = studentData[0].trim();
            if (!fields[field]) {
              fields[field] = [];
            }
            fields[field].push(name);
            totalStudents += 1;
          }
        });

        let output = `Number of students: ${totalStudents}\n`;
        for (const [field, names] of Object.entries(fields)) {
          output += `Number of students in ${field}: ${names.length}. List: ${names.join(', ')}\n`;
        }
        resolve(output.trim()); // Remove trailing newline
      }
    });
  });
};

// Route for /
app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});

// Route for /students
app.get('/students', (req, res) => {
  const database = process.argv[2]; // Get the database from command-line argument
  if (!database) {
    res.status(500).send('No database provided');
    return;
  }

  countStudents(database)
    .then((studentsData) => {
      res.send(`This is the list of our students\n${studentsData}`);
    })
    .catch((err) => {
      res.status(500).send(err.message);
    });
});

app.listen(port, () => {
  console.log(`Server is listening on port ${port}`);
});

module.exports = app;