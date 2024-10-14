// 3-read_file_async.js
const fs = require('fs').promises;

function countStudents(path) {
    return fs.readFile(path, 'utf8')
        .then((data) => {
            const rows = data.trim().split('\n');

            if (rows.length <= 1) {
                throw new Error('Cannot load the database');
            }

            const studentData = rows.slice(1).filter(row => row.trim() !== '');

            console.log(`Number of students: ${studentData.length}`);

            const fields = {};

            studentData.forEach((row) => {
                const [firstname, lastname, age, field] = row.split(',');

                if (!fields[field]) {
                    fields[field] = [];
                }

                fields[field].push(firstname);
            });

            for (const field in fields) {
                const studentsInField = fields[field];
                console.log(`Number of students in ${field}: ${studentsInField.length}. List: ${studentsInField.join(', ')}`);
            }
        })
        .catch(() => {
            throw new Error('Cannot load the database');
        });
}

module.exports = countStudents;
