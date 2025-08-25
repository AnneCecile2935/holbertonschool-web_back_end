# ES6 Data Manipulation

**Projet Holberton** – Manipulation de données avec ES6 : Array, Typed Array, Set, Map, WeakMap

---

## 📚 Ressources

- [Array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array)
- [Typed Array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Typed_arrays)
- [Set Data Structure](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set)
- [Map Data Structure](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map)
- [WeakMap](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/WeakMap)

---

## 🎯 Objectifs d'apprentissage

À la fin de ce projet, tu seras capable d'expliquer **sans Google** :

- Comment utiliser `map`, `filter` et `reduce` sur les tableaux.
- Les **Typed Arrays** et leur utilisation.
- Les structures de données **Set**, **Map**, et les liens faibles (**WeakMap**).

---

## 🛠 Configuration

### Environnement

- **OS** : Ubuntu 20.04 LTS
- **Node.js** : 20.x.x
- **npm** : 9.x.x
- **Éditeurs autorisés** : vi, vim, emacs, Visual Studio Code

### Installation

1. **NodeJS 20.x.x** :

   ```bash
   curl -sL https://deb.nodesource.com/setup_20.x -o nodesource_setup.sh
   sudo bash nodesource_setup.sh
   sudo apt install nodejs -y

### Cas pratiques


| Tâche | Fichier à créer                          | Objectif                                                                                     | Méthode/Concept clé       | Exemple de sortie                                                                                     |
|-------|------------------------------------------|----------------------------------------------------------------------------------------------|---------------------------|--------------------------------------------------------------------------------------------------------|
| 0     | `0-get_list_students.js`                 | Retourner un tableau d'objets étudiants (id, firstName, location).                           | Tableaux, objets          | `[{ id: 1, firstName: 'Guillaume', location: 'San Francisco' }, ...]`                                |
| 1     | `1-get_list_student_ids.js`              | Extraire les IDs des étudiants avec `map`. Retourne `[]` si l'argument n'est pas un tableau. | `map`                     | `[1, 2, 5]`                                                                                           |
| 2     | `2-get_students_by_loc.js`               | Filtrer les étudiants par ville avec `filter`.                                               | `filter`                  | `[{ id: 1, firstName: 'Guillaume', location: 'San Francisco' }, ...]`                                |
| 3     | `3-get_ids_sum.js`                       | Calculer la somme des IDs des étudiants avec `reduce`.                                       | `reduce`                  | `8`                                                                                                    |
| 4     | `4-update_grade_by_city.js`              | Mettre à jour les notes des étudiants d'une ville spécifique (combiner `filter` et `map`).  | `filter`, `map`           | `[{ id: 1, firstName: 'Guillaume', location: 'San Francisco', grade: 86 }, ...]`                     |
| 5     | `5-typed_arrays.js`                      | Créer un `ArrayBuffer` avec une valeur `Int8` à une position donnée.                         | Typed Arrays              | `DataView { byteLength: 10, buffer: ArrayBuffer { [Uint8Contents]: <00 00 59 00 00 00 00 00 00 00> } }` |
| 6     | `6-set.js`                               | Convertir un tableau en `Set`.                                                               | `Set`                     | `Set { 12, 32, 15, 78, 98 }`                                                                           |
| 7     | `7-has_array_values.js`                  | Vérifier si tous les éléments d'un tableau existent dans un `Set`.                            | `Set`, boucles            | `true` / `false`                                                                                      |
| 8     | `8-clean_set.js`                         | Construire une chaîne à partir des valeurs d'un `Set` commençant par une sous-chaîne.       | `Set`, manipulation string| `jovi-aparte-appetit`                                                                                  |
| 9     | `9-groceries_list.js`                    | Créer une `Map` avec des courses et leurs quantités.                                         | `Map`                     | `Map { 'Apples' => 10, 'Tomatoes' => 10, ... }`                                                       |
| 10    | `10-update_uniq_items.js`                | Mettre à jour les quantités à 100 pour les entrées avec une quantité initiale de 1.          | `Map`, gestion d'erreurs  | `Map { 'Pasta' => 100, 'Rice' => 100, ... }`                                                          |

### Author

Anne-Cécile Colléter
