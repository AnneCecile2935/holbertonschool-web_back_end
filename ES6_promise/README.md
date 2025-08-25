# ES6 Promise

**Auteur** : [Annececile Colleter](https://github.com/ton-profil-github)
**Projet** : Holberton School – Web Back-end
**Date** : Août 2025

---

## 📚 Ressources

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)
- [JavaScript Promise: An Introduction](https://web.dev/articles/promises)
- [Async/Await](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Asynchronous/Async_await)
- [Throw/Try](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/throw)

---

## 🎯 Objectifs d'apprentissage

À la fin de ce projet, tu seras capable d'expliquer **sans Google** :

- Les **Promesses** (comment, pourquoi, et quoi).
- Utilisation des méthodes `then`, `resolve`, `catch`.
- Toutes les méthodes de l'objet `Promise`.
- L'opérateur `await` et les fonctions `async`.
- Gestion des erreurs avec `throw`/`try`.

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


| Tâche | Fichier à créer          | Objectif                                                                                     | Concepts/Méthodes clés            | Exemple de sortie / Comportement attendu                                                                 |
|-------|--------------------------|----------------------------------------------------------------------------------------------|-----------------------------------|----------------------------------------------------------------------------------------------------------|
| 0     | `0-promise.js`           | Créer et retourner une Promesse via `getResponseFromAPI()`.                                   | `Promise`                         | `true` (vérification avec `instanceof Promise`)                                                          |
| 1     | `1-promise.js`           | Retourner une Promesse résolue (si `success=true`) ou rejetée (si `success=false`).           | `resolve`, `reject`               | **Résolu** : `{ status: 200, body: 'Success' }`<br>**Rejeté** : `Error: The fake API is not working currently` |
| 2     | `2-then.js`              | Ajouter 3 gestionnaires à une Promesse : résolution, rejet, et log "Got a response from the API". | `then`, `catch`, `finally`        | Affiche `Got a response from the API` dans la console.                                                   |
| 3     | `3-all.js`               | Résoudre `uploadPhoto` et `createUser` (depuis `utils.js`) et afficher `body firstName lastName`. Gérer l'erreur avec "Signup system offline". | `Promise.all`                     | `photo-profile-1 Guillaume Salva`                                                                       |
| 4     | `4-user-promise.js`      | Retourner une Promesse résolue avec un objet `{ firstName, lastName }`.                       | Promesse résolue                  | `Promise { { firstName: 'Bob', lastName: 'Dylan' } }`                                                    |
| 5     | `5-photo-reject.js`      | Retourner une Promesse rejetée avec le message `$fileName cannot be processed`.               | `reject`                          | `Promise { <rejected> Error: guillaume.jpg cannot be processed }`                                        |
| 6     | `6-final-user.js`        | Gérer 2 promesses (`signUpUser` et `uploadPhoto`) et retourner un tableau avec leur statut/valeur. | `Promise.allSettled`              | `[{ status: 'fulfilled', value: {...} }, { status: 'rejected', reason: Error(...) }]`                   |
| 7     | `7-load_balancer.js`     | Retourner la valeur de la Promesse résolue en premier entre deux promesses.                  | `Promise.race`                    | `Downloading from UK is faster` (selon la promesse la plus rapide)                                      |
| 8     | `8-try.js`               | Diviser deux nombres. Lancer une erreur si le dénominateur est 0.                             | `throw`                           | **Succès** : `5`<br>**Erreur** : `Error: cannot divide by 0`                                              |
| 9     | `9-try.js`               | Exécuter une fonction math et retourner un tableau avec le résultat ou l'erreur, suivi de "Guardrail was processed". | `try`/`catch`                     | **Succès** : `[5, 'Guardrail was processed']`<br>**Erreur** : `['Error: cannot divide by 0', 'Guardrail was processed']` |

### Author

Anne-Cécile Colléter
