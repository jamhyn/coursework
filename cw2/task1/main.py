def cyclicShift(message, shift):
    if not message or shift < 0 or shift >= len(message):
        return message

    shift = shift % len(message)

    return message[-shift:] + message[:-shift]

def decryptCyclicShift(message, shift):
    if not message or shift < 0 or shift >= len(message):
        return message