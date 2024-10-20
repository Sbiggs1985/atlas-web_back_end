const fs = require('fs');

const readDatabase = (filePath) => {
  return new Promise((resolve, reject) => {
    fs.readFile(filePath, 'utf-8', (err, data) => {
      if (err) {
        reject(new Error('Cannot load the database'));
        return;
      }

      const lines = data.split('\n').filter(line => line.trim() !== '');
      const students = {};

      // Skip the header
      lines.slice(1).forEach((line) => {
        const [firstname, , , field] = line.split(',');
        if (!students[field]) students[field] = [];
        students[field].push(firstname);
      });

      resolve(students);
    });
  });
};

export default readDatabase;