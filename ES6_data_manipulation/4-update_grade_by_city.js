export default function updateStudentGradeByCity(students, city, newGrades) {
// filtrer les étudiants par ville
  const studentsInCity = students.filter((student) => student.location === city);
  // AJouter les notes avec map
  return studentsInCity.map((student) => {
    // trouver la note de l'étudiant dans newGrades
    const gradeObj = newGrades.find((grade) => grade.studentId === student.id);
    // retourner un nouvel objet avec la note ou n/A
    return {
      ...student, // copie des pptés de l'étudiant
      grade: gradeObj ? gradeObj.grade : 'N/A',

    };
  });
}
