# 📱 Phone Number Information Extractor

This project allows you to extract useful metadata from phone numbers using the Python `phonenumbers` library. It provides details such as:

- 🌍 Geographical location
- ⏰ Time zones
- 📡 Carrier information
- ✅ Validity checks

---

## 🚀 Features

- Parse and format phone numbers.
- Get region and carrier details.
- Validate if the phone number is valid.
- Handle errors gracefully when parsing invalid numbers.

---

## 🛠 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/AkshayKondke/Python-Projects.git
   ```
2. Navigate to the project directory:
   ```bash
   cd PhoneNumber Information Project
   ```
3. Install dependencies:
   ```bash
   pip install phonenumbers
   ```

---

## 📄 Usage

Run the script and input a phone number with the country code (e.g., `+1XXXXXXXXXX`):

```bash
python phone_info_extractor.py
```

### Example Input
```text
Enter your number with +__: +14155552671
```

### Example Output
```text
Phone Number :  Country Code: 1 National Number: 4155552671
Timezone(s) :  ('America/Los_Angeles',)
Carrier :  AT&T
Region :  California
```

---

## 🧩 Code Explanation

### Key Libraries Used

- `phonenumbers`: A library for parsing, formatting, and validating phone numbers.

### Code Highlights

- **Phone Number Parsing:**
  Parses the user input into a structured phone number object.
  ```python
  phone = phonenumbers.parse(number)
  ```

- **Error Handling:**
  Gracefully handles invalid inputs using try-except blocks.
  ```python
  except phonenumbers.NumberParseException as e:
      print(f"Error while parsing number: {e}")
  ```

- **Geographical and Carrier Details:**
  Retrieves the location and carrier associated with the number.
  ```python
  register = geocoder.description_for_number(phone, "en")
  car = carrier.name_for_number(phone, "en")
  ```

- **Validity Checks:**
  Confirms if the number is valid.
  ```python
  if phonenumbers.is_valid_number(phone):
  ```

---

## 📂 File Structure

```
PhoneNumber Information Project/
├── phone_info_extractor.py   # Main script
└── README.md                 # Project documentation
```

---

## 📜 License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## 🤝 Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request.

---

## 🌟 Acknowledgements

- Thanks to the developers of the `phonenumbers` library for their fantastic work.

---

## 📧 Contact

- GitHub: [AkshayKondke](https://github.com/AkshayKondke/Python-Projects.git)
- Email: default.cyber009@gmail.com
