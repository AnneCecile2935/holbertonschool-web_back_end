const fs = require('fs').promises;

function countStudents(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf-8')
      .then((data) => {
        const lines = data.split('\n').filter((line) => line.trim() !== '');
        const students = lines.slice(1);
        const studentsByField = {};
        let totalStudents = 0;

        for (const line of students) {
          const [firstname, , , field] = line.split(',');
          if (firstname && field) {
            totalStudents += 1;
            if (!studentsByField[field]) {
              studentsByField[field] = [];
            }
            studentsByField[field].push(firstname);
          }
        }

        console.log(`Number of students: ${totalStudents}`);
        for (const [field, firstnames] of Object.entries(studentsByField)) {
          console.log(`Number of students in ${field}: ${firstnames.length}. List: ${firstnames.join(', ')}`);
        }
        resolve();
      })
      .catch(() => {
        reject(new Error('Cannot load the database'));
      });
  });
}

module.exports = countStudents;
