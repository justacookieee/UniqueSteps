
# Unique Steps

## Overview
UniqueSteps is a class for comparing sequences for a specific application between two regions or just extracting information about sequences for an application in a region.

Currently supported categories of steps:

- **Failed Steps**
- **Passed Steps**
- **Steps in Progress**
- **Not Applicable Steps**

Support in the future
- **Steps Not Executed**

---

## Prerequisites
Before using the tool, ensure you have:
- **Python 3.8+** installed
- Required libraries (see [Installation](#installation))

---

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/justacookieee/UniqueSteps.git
   ```
2. Navigate to the project directory:
   ```bash
   cd UniqueSteps
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Create a .env file with your OTTR credentials
	```
	OTTR_USERNAME=name
	OTTR_PASS=password
	``` 

---

## Usage
1. Modify v1.py file according to your requirements
2. Run v1.py from the terminal.
   ```bash
   python UniqueSteps.py
   ```

---

## Contributing
Contributions are welcome! If you have ideas for improvement, please fork the repository and submit a pull request.

---

## License
This project is licensed under the [MIT License](LICENSE).
