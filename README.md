# pyhash GUI

A simple GUI application to generate hashed passwords using various hashing algorithms. The application is built using Python's `tkinter` library and supports SHA-256, SHA-1, MD5, SHA-512, SHA-384, and SHA-224 hashing algorithms.

## Features

- Input a password and generate its hash using the selected algorithm.
- Supports multiple hashing algorithms: SHA-256, SHA-1, MD5, SHA-512, SHA-384, and SHA-224.
- Copy the generated hash to the clipboard with a single click.

## Prerequisites

- Python 3.x

## Installation

1. Clone the repository or download the source code.

    ```bash
    git clone https://github.com/zanesense/pyhash-gui.git
    cd pyhash-gui
    ```

2. Run the application.

    ```bash
    python hasher.py
    ```

## Usage

1. Open the application.
2. Enter the password you want to hash in the "Enter Password" field.
3. Select the desired hashing algorithm from the dropdown menu.
4. Click the "Generate Hash" button to generate the hashed password.
5. The hashed password will be displayed in the text box below.
6. To copy the hashed password to the clipboard, click the "Copy to Clipboard" button.

## Code Explanation

### `generate_hash()`

This function retrieves the password from the input field and the selected hashing algorithm from the dropdown menu. It then generates the hashed password using the specified algorithm and displays it in the output text box.

### `copy_to_clipboard()`

This function copies the generated hashed password to the clipboard.

### GUI Components

- `password_label` and `password_entry`: Input field for entering the password.
- `hash_option` and `hash_dropdown`: Dropdown menu for selecting the hashing algorithm.
- `generate_button`: Button to generate the hashed password.
- `output_label` and `hash_output`: Text box to display the generated hashed password.
- `copy_button`: Button to copy the hashed password to the clipboard.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
