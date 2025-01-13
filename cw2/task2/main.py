def cyclic_shift(m, shift):
    # Cyclically shifts m by shift (number of) positions to the right
    if not m or shift < 0 or shift >= len(m):
        return m
    shift = shift % len(m)
    return m[-shift:] + m[:-shift]


def encrypt_message(key, message):
    # Validate the encryption key and make sure it is 6 characters
    if len(key) != 6:
        print("Encryption key must be 6 characters long.")

    # Pad the message to a multiple of 8
    while len(message) % 8 != 0:
        message += 'a'

    # Split the message into subsequences of length 8
    subsequences = [message[i:i + 8] for i in range(0, len(message), 8)]

    # Calculate shift1
    shift1 = (ord(key[0]) + ord(key[1])) % 8

    # Perform right cyclic shift on each subsequence of 8 using shift1
    shifted_subsequences = [cyclic_shift(subseq, shift1) for subseq in subsequences]

    # Calculate shift2
    shift2 = (ord(key[2]) + ord(key[3])) % 3

    # Perform cyclic shift on the list of subsequences using shift2
    shifted_list = cyclic_shift(shifted_subsequences, shift2)

    # Concatenate all subsequences to form the encrypted message
    encrypted_message = ''.join(shifted_list)

    return encrypted_message


# Main function to run the encryption
def main():
    # Ask for user input for encryption key
    key = input("Enter a 6-character encryption key: ")
    if len(key) != 6:
        print("Error: The key must be exactly 6 characters long.")
        return

    message = input("Enter the message to encrypt: ")
    print("\nMessage encrypted successfully")
    encrypted_message = encrypt_message(key, message)
    print("Encrypted Message:", encrypted_message)


# Run the main function
if __name__ == "__main__":
    main()