export default function createReportObject(employeesList) {
  const report = Object.assign({}, {
    allEmployees: { ...employeesList },
    getNumberOfDepartments() {
      return Object.keys(this.allEmployees).length;
    }
  });
  return report;
}
