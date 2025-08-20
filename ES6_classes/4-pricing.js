import Currency from './3-currency'; // Import de la classe Currency

export default class Pricing {
  constructor(amount, currency) {
    // Vérifie que amount est bien un nombre
    if (typeof amount !== 'number') {
      throw new TypeError('amount must be a number');
    }

    // Vérifie que currency est une instance de Currency
    if (!(currency instanceof Currency)) {
      throw new TypeError('currency must be an instance of Currency');
    }

    this._amount = amount; // Stockage du montant avec underscore
    this._currency = currency; // Stockage de la devise avec underscore
  }

  // Getter pour l'attribut amount
  get amount() {
    return this._amount;
  }

  // Setter pour l'attribut amount avec vérification du type
  set amount(value) {
    if (typeof value !== 'number') {
      throw new TypeError('amount must be a number');
    }
    this._amount = value;
  }

  // Getter pour l'attribut currency
  get currency() {
    return this._currency;
  }

  // Setter pour l'attribut currency avec vérification du type
  set currency(value) {
    if (!(value instanceof Currency)) {
      throw new TypeError('currency must be an instance of Currency');
    }
    this._currency = value;
  }

  /**
   * Méthode d'instance pour afficher le prix complet
   * @returns {string} - Format : "amount currency_name (currency_code)"
   */
  displayFullPrice() {
    return `${this._amount} ${this._currency.name} (${this._currency.code})`;
  }

  /**
   * Méthode statique pour convertir un montant avec un taux de conversion
   * @param {number} amount - Montant à convertir
   * @param {number} conversionRate - Taux de conversion
   * @returns {number} - Montant converti
   */
  static convertPrice(amount, conversionRate) {
    if (typeof amount !== 'number' || typeof conversionRate !== 'number') {
      throw new TypeError('amount and conversionRate must be numbers');
    }
    return amount * conversionRate;
  }
}
