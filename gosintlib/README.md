# **G-Osintlib**

This Python script contains several functions designed to validate and retrieve detailed information for various data types such as phone numbers, IP addresses, credit cards, email addresses, VINs, ISINs, ISBNs, and IP cameras. These functions utilize third-party APIs and libraries to fetch relevant data, enabling quick and efficient data lookups.

---

## Table of Contents

1. [Functions Overview](#functions-overview)
2. [Function Details](#function-details)
3. [Requirements](#requirements)
4. [Usage](#usage)
5. [Error Handling](#error-handling)
6. [License](#license)
7. [Credits](#credits)

---

## Functions Overview

The script includes the following functions:

- **phone(number)**: Validates and retrieves information about a phone number.
- **ipscan(ip, fast=False)**: Performs an IP scan and retrieves geolocation and open port information.
- **creditcard(card)**: Validates and retrieves information about a credit card.
- **email(email)**: Validates an email address and checks for a valid mail server.
- **vinscan(vin)**: Retrieves information about a vehicle using its VIN (Vehicle Identification Number).
- **isin(isin)**: Validates and retrieves information about an ISIN (International Securities Identification Number).
- **isbn(isbn)**: Validates and retrieves information about a book using its ISBN.
- **ipcams(countrycode)**: Retrieves IP addresses of public IP cameras in a given country.
- **ipcamscode()**: Displays a list of countries and the number of webcams available in each country.

---

## Function Details

### `phone(number)`

- **Description**: Validates a phone number and retrieves details such as country, carrier, time zone, and international format.
- **Input**: A phone number as a string.
- **Output**: Displays phone number information including country, carrier, and time zone.

---

### `ipscan(ip, fast=False)`

- **Description**: Scans an IP address, retrieves location information, and performs port scanning (optional).
- **Input**: IP address (string), `fast` (boolean) to skip port scanning.
- **Output**: Prints IP information such as location, organization, and open ports (if `fast` is set to `False`).

---

### `creditcard(card)`

- **Description**: Validates a credit card number using the Luhn algorithm and retrieves card information from BIN (Bank Identification Number).
- **Input**: A credit card number as a string.
- **Output**: Prints card details such as type, brand, issuer, country, and currency.

---

### `email(email)`

- **Description**: Validates the format of an email address and checks for a valid mail server (MX records).
- **Input**: An email address as a string.
- **Output**: Prints information about the email's domain and mail server validity.

---

### `vinscan(vin)`

- **Description**: Retrieves vehicle information based on the VIN (Vehicle Identification Number).
- **Input**: A VIN as a string.
- **Output**: Prints detailed information about the vehicle, such as make, model, and year.

---

### `isin(isin)`

- **Description**: Validates the format of an ISIN (International Securities Identification Number) and extracts its components.
- **Input**: An ISIN number as a string.
- **Output**: Prints the country code, security identifier, and checksum of the ISIN.

---

### `isbn(isbn)`

- **Description**: Validates the format of an ISBN and retrieves information about the book.
- **Input**: An ISBN number as a string (either ISBN-10 or ISBN-13).
- **Output**: Prints information about the book based on the ISBN format.

---

### `ipcams(countrycode)`

- **Description**: Retrieves the IP addresses of publicly available IP cameras from a specific country.
- **Input**: Country code (ISO 3166-1 alpha-2).
- **Output**: Prints a list of IP camera IP addresses from the country specified and saves the results to a `.txt` file.

---

### `ipcamscode()`

- **Description**: Displays a list of countries and the number of webcams available in each country.
- **Input**: None.
- **Output**: Prints the country code, country name, and the number of webcams in each country.

---

## Requirements

To run this script, you will need to install the following Python packages:

- `phonenumbers`: For phone number validation and information.
- `requests`: For making HTTP requests to external APIs.
- `socket`: For resolving IP addresses.
- `dns.resolver`: For resolving MX records for email validation.
- `re`: For regular expressions to validate ISIN, ISBN, and email formats.
- `concurrent.futures`: For multi-threaded port scanning.
- `colorama`: For color formatting in the terminal.

You can install the required packages using the following command:

```bash
pip install phonenumbers requests dnspython colorama
```

---

## Usage

To use the script, simply call one of the functions with the appropriate input. For example:

### Example 1: Phone Number

```python
phone("+14155552671")
```

### Example 2: IP Scan

```python
ipscan("8.8.8.8", fast=True)
```

### Example 3: Credit Card

```python
creditcard("4111111111111111")
```

### Example 4: Email

```python
email("example@example.com")
```

### Example 5: VIN Scan

```python
vinscan("1HGCM82633A123456")
```

### Example 6: ISIN

```python
isin("US0378331005")
```

### Example 7: ISBN

```python
isbn("9780132350884")
```

### Example 8: IP Cameras in a Country

```python
ipcams("US")
```

### Example 9: List of Countries and Webcams

```python
ipcamscode()
```

---

## Error Handling

The functions handle various exceptions gracefully, including:

- **Invalid Format**: If the input does not match the expected format (e.g., a malformed phone number, VIN, or credit card), an error message will be shown.
- **Network Issues**: If there is a problem with the external API or network, the script will output a relevant error message.
- **Invalid Data**: If the data retrieved from an API is invalid or incomplete, the script will print an error message, prompting the user to try again or verify the data.

---

## License

This script is released under the MIT License. Feel free to modify and distribute it as needed.

---

## Credits

This script was created by **LemonPower21** (also known as **Francesco Vito Giotta**).

---