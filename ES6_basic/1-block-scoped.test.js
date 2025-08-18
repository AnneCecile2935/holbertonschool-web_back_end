import taskBlock from './1-block-scoped.js';

test('taskBlock returns correct values', () => {
  expect(taskBlock(true)).toEqual([false, true]);
  expect(taskBlock(false)).toEqual([false, true]);
});
