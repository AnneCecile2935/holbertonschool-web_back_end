import readDatabase from '../utils';

export default class StudentsController {
  static async getAllStudents(request, response) {
    try {
      const studentsByField = await readDatabase(process.argv[2]);
      let output = 'This is the list of our students\n';

      const totalStudents = Object.values(studentsByField).reduce(
        (acc, students) => acc + students.length,
        0,
      );
      output += `Number of students: ${totalStudents}\n`;

      const fields = Object.keys(studentsByField).sort((a, b) =>
        a.localeCompare(b, { sensitivity: 'base' })
      );

      for (const field of fields) {
        output += `Number of students in ${field}: ${studentsByField[field].length}. List: ${studentsByField[field].join(', ')}\n`;
      }
      return response.status(200).send(output);
    } catch (error) {
      return response.status(500).send('Cannot load the database');
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
      return response.status(200).send(`List: ${firstnames.join(', ')}`);
    } catch (error) {
      return response.status(500).send('Cannot load the database');
    }
  }
}
