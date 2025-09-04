import readDatabase from '../utils';

export default class StudentsController {
  static async getAllStudents(request, response) {
    try {
      const studentsByField = await readDatabase(process.argv[2]);
      let output = 'This is the list of our students\n';

      const fields = Object.keys(studentsByField).sort((a, b) => a.localeCompare(b, undefined, { sensitivity: 'base' }));
      const totalStudents = Object.values(studentsByField).reduce(
        (acc, students) => acc + students.length,
        0,
      );
      output += `Number of students: ${totalStudents}\n`;
      for (const field of fields) {
        const firstnames = studentsByField[field];
        output += `Number of students in ${field}: ${firstnames.length}. List: ${firstnames.join(', ')}\n`;
      }
      response.status(200).set('Content-Type', 'text/plain').send(output);
    } catch (error) {
      response.status(500).set('Content-Type', 'text/plain').send('Cannot load the database');
    }
  }

  static async getAllStudentsByMajor(request, response) {
    const { major } = request.params;
    if (major !== 'CS' && major !== 'SWE') {
      return response.status(500).send('Major parameter must be CS or SWE');
    }

    try {
      const studentsByField = await readDatabase(process.argv[2]);
      const firstnames = studentsByField[major] || [];
      return response.status(200).set('Content-Type', 'text/plain').send(`List: ${firstnames.join(', ')}`);
    } catch (error) {
      return response.status(500).set('Content-Type', 'text/plain').send('Cannot load the database');
    }
  }
}
