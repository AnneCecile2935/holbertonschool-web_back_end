import fs from 'fs';

export default function readDatabase(filePath) {
  return new Promise((resolve, reject) => {
    fs.readFile(filePath, 'utf-8', (err, data) => {
      if (err) {
        reject(new Error('Cannot load the database'));
        return;
      }

      const lines = data.split('\n').filter((line) => line.trim() !== '');
      const students = lines.slice(1);
      const studentsByField = {};

      for (const line of students) {
        const [firstname, , , field] = line.split(',');
        if (firstname && field) {
          if (!studentsByField[field]) studentsByField[field] = [];
          studentsByField[field].push(firstname);
        }
      }

      resolve(studentsByField);
    });
  });
}
