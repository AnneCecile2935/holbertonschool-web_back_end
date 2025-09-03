const fs = require('fs').promises;

function countStudents(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf-8')
      .then((data) => {
        const lines = data.split('\n').filter((line) => line.trim() !== '');
        const students = lines.slice(1); // Ignore l'en-tête
        const studentsByField = {};
        let output = `Number of students: ${students.length}\n`;

        for (const line of students) {
          const [firstname, , , field] = line.split(',');
          if (firstname && field) {
            if (!studentsByField[field]) {
              studentsByField[field] = [];
            }
            studentsByField[field].push(firstname);
          }
        }

        for (const [field, firstnames] of Object.entries(studentsByField)) {
          output += `Number of students in ${field}: ${firstnames.length}. List: ${firstnames.join(', ')}\n`;
        }

        resolve(output);
      })
      .catch(() => {
        reject(new Error('Cannot load the database'));
      });
  });
}

module.exports = countStudents;
