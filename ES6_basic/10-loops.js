export default function appendToEachArrayValue(array, appendString) {
	const newArray = []
  for (const value in array) {
    newArray.push(appendString + value);
  }

  return array;
}
