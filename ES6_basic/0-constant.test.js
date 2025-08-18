import { myFunction } from './0-module.js';

test('myFunction should return the correct string', () => {
  expect(myFunction()).toBe("I prefer const when I can. But sometimes let is okay");
});
