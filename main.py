from encrypt import encrypt, create_matrix, print_matrix, preprocess_text
from decrypt import decrypt

def main():
    print("=" * 50)
    print(" " * 10 + "PLAYFAIR CIPHER ALGORITHM")
    print("=" * 50)
    
    while True:
        print("\nSelect an option:")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Exit")
        
        choice = input("Enter your choice (1/2/3): ")
        
        if choice == '1':
            key = input("\nEnter key: ")
            text = input("Enter plaintext: ")
            
            matrix = create_matrix(key)
            print_matrix(matrix)
            
            encrypted_text = encrypt(text, key)
            print("Processed character pairs:", " ".join(preprocess_text(text)))
            print(f"Ciphertext: {encrypted_text}")
            
        elif choice == '2':
            key = input("\nEnter key: ")
            text = input("Enter ciphertext: ")
            
            matrix = create_matrix(key)
            print_matrix(matrix)
            
            decrypted_text = decrypt(text, key)
            print(f"Decrypted text (may contain 'X'): {decrypted_text}")
            
        elif choice == '3':
            print("Program execution completed!")
            break
        else:
            print("Invalid choice, please try again!")

if __name__ == "__main__":
    main()
