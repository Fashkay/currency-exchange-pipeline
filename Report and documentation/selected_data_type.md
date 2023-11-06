# Selected Data Type

The chosen data type for this project is currency exchange rate data. This type of data is numerical and typically represented as decimals. It involves two currencies and their exchange rate relative to each other.

## Data Attributes

1. **Base Currency**:
   - Data Type: String (VARCHAR)
   - Description: Represents the currency being converted from (e.g., USD for US Dollar).

2. **Target Currency**:
   - Data Type: String (VARCHAR)
   - Description: Represents the currency being converted to (e.g., EUR for Euro).

3. **Exchange Rate**:
   - Data Type: Decimal
   - Description: Represents the exchange rate value, which is a numerical value with precision.

4. **Timestamp**:
   - Data Type: Timestamp
   - Description: Indicates the date and time when the exchange rate data was acquired.

## Rationale for Data Type Selection

The selected data type ensures that the exchange rate data is accurately represented and allows for precise calculations. Using string data types for currencies allows for flexibility in handling various currency codes. The decimal data type is chosen for the exchange rate to maintain accuracy in calculations involving monetary values.

Additionally, the timestamp data type captures the time at which the data was acquired, providing essential temporal context for the exchange rates.

---

This section outlines the chosen data type for the project and provides a detailed explanation of the attributes, their respective data types, and their significance in representing currency exchange rate data accurately. It also includes the rationale behind the selection of each data type.
