import returnHowManyArguments from './4-rest-parameter.js';

test('returnHowManyArguments counts the number of arguments', () => {
  expect(returnHowManyArguments()).toBe(0);
  expect(returnHowManyArguments('Hello')).toBe(1);
  expect(returnHowManyArguments('Hello', 'World')).toBe(2);
  expect(returnHowManyArguments('a', 'b', 'c', 1, 2, 3)).toBe(6);
});
