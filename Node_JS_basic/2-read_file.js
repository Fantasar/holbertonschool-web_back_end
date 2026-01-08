const fs = require('fs');

function countStudents(path) {
    try {
        const data = fs.readFileSync(path, 'utf8');
        const lines = data.split('\n');
        const students = lines.slice(1).filter(line => line.trim() !== '');
        console.log(`Number of students: ${students.length}`);
        const fields = {};

        students.forEach(line => {
            const [firstname, lastname, age, field] = line.split(',');
            if (!fields[field]) {
                fields[field] = [];
            }

            fields[field].push(firstname);
        });
    
        for (const field in fields) {
            const list = fields[field].join(', ');
            console.log(`Number of students in ${field}: ${fields[field].length}. List: ${list}`);
        }

    } catch (error) {
        throw new Error('Cannot load the database');
    }
}

module.exports = countStudents;