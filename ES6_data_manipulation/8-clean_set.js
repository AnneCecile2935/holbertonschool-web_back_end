export default function cleanSet(set, startString) {
  // Si startString est vide, on retourne une chaîne vide
  if (startString === '') return '';

  const result = [];
  for (const item of set) {
    // On vérifie que l'item commence bien par startString
    if (item.startsWith(startString)) {
      // On ajoute la partie après startString
      result.push(item.slice(startString.length));
    }
  }
  // On joint les résultats avec un tiret, sans espace
  return result.join('-');
}
