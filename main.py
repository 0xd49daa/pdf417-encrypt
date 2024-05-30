import sys
import getpass
from encrypt import encrypt_file, generate_pdf417
from decrypt import decrypt_data, read_pdf417

def main():
    if len(sys.argv) < 4:
        print("Usage: python main.py <encrypt/decrypt> <input_path> <output_path>")
        sys.exit(1)

    operation = sys.argv[1].lower()
    input_path = sys.argv[2]
    output_path = sys.argv[3]

    if operation == "encrypt":
        password = getpass.getpass('Enter the password to encrypt: ')
        encrypted_data = encrypt_file(input_path, password)
        generate_pdf417(encrypted_data, output_path)
        print(f'{output_path} successfully generated')
    elif operation == "decrypt":
        password = getpass.getpass('Enter the password to decrypt: ')
        encrypted_data_from_barcode = read_pdf417(input_path)
        if encrypted_data_from_barcode:
            try:
                decrypted_data = decrypt_data(encrypted_data_from_barcode, password)
                with open(output_path, 'wb') as f:
                    f.write(decrypted_data)
                print(f'Data successfully read and decrypted into {output_path}')
            except Exception as e:
                print(f'Decryption failed: {e}')
        else:
            print('Failed to read the barcode.')
    else:
        print("Invalid operation. Use 'encrypt' or 'decrypt'.")

if __name__ == '__main__':
    main()
