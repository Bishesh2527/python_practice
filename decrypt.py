import base64

def xor_decrypt(encrypted_data, key):
    decrypted_data = ''
    key_len = len(key)
    
    # XOR decryption
    for i in range(len(encrypted_data)):
        decrypted_data += chr(encrypted_data[i] ^ ord(key[i % key_len]))  # XOR with the key
        
    return decrypted_data

# Base64 encoded encrypted string (from JavaScript 'encrypted' variable)
encrypted_base64 = "FQkCFR4REhYaLQMYEgIe"

# XOR Key (from JavaScript 'key' variable)
key = "secret"  # Replace this with the actual key used in the JavaScript code

# Decode from base64
encrypted_bytes = base64.b64decode(encrypted_base64)

# Decrypt the data using XOR
decrypted = xor_decrypt(encrypted_bytes, key)

print("Decrypted:", decrypted)