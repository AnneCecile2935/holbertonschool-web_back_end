import {  taskFirst, taskNext} from './0-constants.js';

test('taskFirst should return the correct string', () => {
  expect(taskFirst()).toBe('I prefer const when I can.');
});

test('taskNext should return the correct string', () => {
  expect(taskNext()).toBe('But sometimes let is okay');
});

test('combined output', () => {
  const combined = `${taskFirst()} ${taskNext()}`;
  expect(combined).toBe('I prefer const when I can. But sometimes let is okay');
});
