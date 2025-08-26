export default function createInt8TypeArray(length, position, value) {
  // Allouer un tampon binaire de length octets
  const buffer = new ArrayBuffer(length);
  // créer une vue Int8Array sur le tampon pour écrire des entiers 8 bits
  const dataView = new DataView(buffer);
  // si position nég ou > à length => erreur
  if (position < 0 || position >= length) {
    throw new Error('Position outside range');
  }
  // Écrire la valeur Int8 à la position spécifiée
  dataView.setInt8(position, value);
  // retourner l'arraybuffer
  return dataView;
}
