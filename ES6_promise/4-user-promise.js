export default function signUser(firstName, lastName) {
  return Promise.resolve({
    firstName,
    lastName,
  });
}
