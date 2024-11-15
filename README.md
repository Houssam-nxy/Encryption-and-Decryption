# Simple Encryption and Decryption Tool

A basic Python program that demonstrates a substitution cipher for encrypting and decrypting text. The encryption is based on shifting the letters of the alphabet by a fixed amount.

---

## Features
- **Encrypt Text:** Converts plain text into an encrypted numeric key.
- **Decrypt Text:** Reverts the encrypted numeric key back into the original text.
- Simple and easy-to-understand implementation using Python.

---

## How It Works
1. Each letter in the input is replaced by its position in the alphabet shifted by 6 (e.g., `a` → `g`).
2. Non-alphabetic characters are ignored during encryption.
3. Decryption reverses the process by shifting positions back by 6.

---

## Interaction
The tool runs directly in the terminal with an interactive prompt. Users can choose to encrypt or decrypt text by following these steps:

### Start
When you run the program, it will prompt:
```
Encryption or Decryption (e/d):
```

### For Encryption:
1. Type `e` and press **Enter**.
2. Enter the text you want to encrypt:
   ```
   Enter your text: hello
   ```
3. Output:
   ```
   You entered: -> ** hello **
   Your key is ready -> ** 13 4 11 11 14 **
   ```

### For Decryption:
1. Type `d` and press **Enter**.
2. Enter the numeric key (space-separated):
   ```
   Enter your key: 13 4 11 11 14
   ```
3. Output:
   ```
   Your decrypted text is ready: hello
   ```

### Invalid Input:
If you input anything other than `e` or `d`, the program will notify you:
```
Enter valid character ("e" for encryption / "d" for decryption)
```

---

## Usage
1. Clone the repository:
    ```bash
    git clone [https://github.com/your-username/encryption-tool.git](https://github.com/Houssam-nxy/Encryption-and-Decryption.git)
    ```
2. Run the program:
    ```bash
    python main.py
    ```
3. Follow the on-screen prompts to encrypt or decrypt text.

---

## Example
**Encryption:**
```
Input: hello
Output: You entered: -> ** hello **
        Your key is ready -> ** 13 4 11 11 14 **
```

**Decryption:**
```
Input: 13 4 11 11 14
Output: Your decrypted text is ready: hello
```

---

## Limitations
- The encryption method is **not secure** for sensitive data.
- Non-alphabetic characters are ignored during processing.
- Uses a fixed shift value of 6.

---

## Improvements
- Allow user-defined keys for added flexibility.
- Handle non-alphabetic characters.
- Replace the substitution cipher with a more secure encryption algorithm like AES.

---

## Contributing
Contributions are welcome! Feel free to fork the repository and submit a pull request with improvements or bug fixes.
