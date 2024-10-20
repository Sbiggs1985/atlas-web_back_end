const fs = require('fs').promises;

async function countStudents(path) {
    try {
        const data = await fs.readFile(path, 'utf8');
        const lines = data.trim().split('\n');

        if (lines.length === 0) {
            throw new Error('Cannot load the database');
        }

        // Remove header line
        const students = lines.slice(1).filter(line => line !== '');

        let output = `Number of students: ${students.length}\n`;
        
        const fields = {};

        // Process student's data
        students.forEach(student => {
            const details = student.split(',');

            const firstName = details[0];
            const field = details[details.length - 1];

            if (!fields[field]) {
                fields[field] = [];
            }
            fields[field].push(firstName);
        });

        // Create output string for each field
        for (const field in fields) {
            const studentList = fields[field].join(', ');
            output += `Number of students in ${field}: ${fields[field].length}. List: ${studentList}\n`;
        }

        return output.trim(); // return the formatted result as a string
    } catch (error) {
        throw new Error('Cannot load the database');
    }
}

module.exports = countStudents;