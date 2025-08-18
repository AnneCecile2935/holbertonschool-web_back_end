export default function taskBlock(trueOrFalse) {
  let task = false;
  let task2 = true;

  if (trueOrFalse) {
    let task = true;   // nouvelle variable locale
    let task2 = false; // nouvelle variable locale
  }

  return [task, task2];
}
