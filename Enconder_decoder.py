def password_encoder(password):
    if len(password) == 8 and password.isdigit():
        return ''.join(str((int(char) + 3) % 10) for char in password)
    else:
        return "Invalid password. Ensure it is an 8-digit integer."

def password_decoder(encoded_password):
    pass

