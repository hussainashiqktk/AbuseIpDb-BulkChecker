# AbuseIPDB Bulk Checker

A simple and efficient tool to check multiple IP addresses against the AbuseIPDB API to retrieve information such as abuse confidence scores, ISP details, and more.

This project uses the **AbuseIPDB** API to help you identify suspicious or malicious IP addresses. It features a **Graphical User Interface (GUI)** built with **Tkinter** for ease of use, allowing you to bulk check IP addresses, view detailed results, and track progress.

---

## 📋 Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [API Key Setup](#api-key-setup)
- [Contributing](#contributing)
- [License](#license)

---

## ✨ Features

- **Bulk IP Check**: Check multiple IP addresses at once.
- **Progress Bar**: Track progress as IPs are being checked.
- **Results Table**: View detailed information in a clean tabular format.
- **Output Box**: Displays additional status information and errors during the checking process.
- **Error Handling**: Handles various API errors and exceptions.

---

## 🛠️ Installation

To get started, you need to install the following dependencies:

### Prerequisites

- **Python 3.x**: Ensure Python is installed on your system.
- **Requests Library**: Used to make API calls to AbuseIPDB.
- **Tkinter**: Python's standard GUI library, used for creating the graphical interface.

You can install the required packages using `pip`:

```bash
pip install requests
```

Tkinter is usually bundled with Python, but if not, you may need to install it manually, depending on your OS.

---

## 🚀 Usage

1. **Clone the repository** or download the script.

2. **Run the script**:

```bash
python bulk_ip_checker.py
```

3. **Enter IP addresses** you want to check (one per line) in the text box provided in the GUI.

4. **Click "Check IPs"** to start checking the IPs against the AbuseIPDB API.

5. The results will be shown in a table format, and you can monitor the progress using the progress bar.

6. You can also view detailed output in the "Output" section.

![2024-11-29_15-49](https://github.com/user-attachments/assets/f3ea38a4-52b4-4bdf-b0c1-8aa459febf9a)


---

## 🔑 API Key Setup

This script requires an **AbuseIPDB API key** to function. Follow these steps to set it up:

1. Visit [AbuseIPDB](https://www.abuseipdb.com/) and sign up for an account.
2. Once logged in, go to your **API Key** section and copy your key.
3. Paste the API key into the script:

```python
api_key = "your_api_key_here"
```

---

## 🧑‍💻 Contributing

We welcome contributions! If you'd like to contribute to this project, feel free to:

1. Fork the repository.
2. Create a new branch for your changes.
3. Commit your changes and push to your forked repository.
4. Open a pull request with a detailed description of your changes.

---

Happy IP checking! 🎉
