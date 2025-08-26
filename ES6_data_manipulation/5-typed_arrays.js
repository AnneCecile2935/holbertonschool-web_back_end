
export default function createInt8TypeArray(length, position, value){
  // Allouer un tampon binaire de length octets
	const buffer = new ArrayBuffer (length);
  // créer une vue Int8Array sur le tampon pour écrire des entiers 8 bits
	const int8Array = new Int8Array(buffer);
  // si position nég ou > à length => erreur
	if (position < 0 || position >= length) {
		throw new Error('Position outside range');
	}
  // écrire la valeur à la position spécifiée
	int8Array[position] = value;
  // retourner l'arraybuffer
	return buffer;
}
