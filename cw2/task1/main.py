def cyclic_shift(m, shift):
    # Make sure that m (message/string) isn't empty and that the shift is valid (a number)
    if not m or shift < 0 or shift >= len(m):
        return m

    # Ensure that the shift value is wrapped around to stay in the range of indices for the input m (message/string)
    shift = shift % len(m)

    # Perform the cyclic shift by extracting the last shift of m and appending it by adding the remainder to give the encrypted message
    return m[-shift:] + m[:-shift]


# Decryption Function
def decrypt_cyclic_shift(m, shift):
    if not m or shift < 0 or shift >= len(m):
        return m

    # Decrypt by reversing the shift
    return cyclic_shift(m, len(m) - (shift % len(m)))


# Tests (each second argument after print(cyclic_shift) is the amount a string is shifted from the end)
def test_cyclic_shift():
    print("String Test:")
    print(cyclic_shift("This is a secret message", 2))  # Expected: "geThis is a secret messa"

    print("List of Numbers Test:")
    print(cyclic_shift([1, 2, 3, 4, 5], 2))  # Expected: [4, 5, 1, 2, 3]

    print("List of Strings Test:")
    print(cyclic_shift(["a", "b", "c", "d"], 1))  # Expected: ["d", "a", "b", "c"]

    print("List of Lists Test:")
    print(cyclic_shift([[1, 2], [3, 4], [5, 6]], 2))  # Expected: [[3, 4], [5, 6], [1, 2]]

    print("Decryption Test:")
    encrypted = cyclic_shift("This is a secret message", 2)
    print("Encrypted:", encrypted)  # Expected: "geThis is a secret messa"
    print("Decrypted:", decrypt_cyclic_shift(encrypted, 2))  # Expected: "This is a secret message"


# Run the function / each test
test_cyclic_shift()