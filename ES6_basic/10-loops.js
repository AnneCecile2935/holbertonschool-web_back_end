export default function appendToEachArrayValue(array, appendString) {
  const newArray = array;
  for (const value of array) {
    const index = array.indexOf(value);
    newArray[index] = appendString + value;
  }
  return newArray;
}
