Simple Encryption and Decryption Tool
A basic Python program that demonstrates a substitution cipher for encrypting and decrypting text. The encryption is based on shifting the letters of the alphabet by a fixed amount.

Features
Encrypt Text: Converts plain text into an encrypted numeric key.
Decrypt Text: Reverts the encrypted numeric key back into the original text.
Simple and easy-to-understand implementation using Python.
How It Works
Each letter in the input is replaced by its position in the alphabet shifted by 6 (e.g., a → g).
Non-alphabetic characters are ignored during encryption.
Decryption reverses the process by shifting positions back by 6.
Usage
Clone the repository:
bash
Copier le code
git clone [https://github.com/your-username/encryption-tool](https://github.com/Houssam-nxy/Encryption-and-Decryption).git
Run the program:
bash
Copier le code
python encryption_tool.py
Follow the prompts to encrypt or decrypt text.
Example
Encryption:

vbnet
Copier le code
Input: hello
Output: You entered: -> ** hello **
        Your key is ready -> ** 13 4 11 11 14 **
Decryption:

vbnet
Copier le code
Input: 13 4 11 11 14
Output: Your decrypted text is ready: hello
Limitations
The encryption method is not secure for sensitive data.
Non-alphabetic characters are ignored during processing.
Uses a fixed shift value of 6.
Improvements
Allow user-defined keys for added flexibility.
Handle non-alphabetic characters.
Replace the substitution cipher with a more secure encryption algorithm like AES.
Contributing
Contributions are welcome! Feel free to fork the repository and submit a pull request with improvements or bug fixes.
