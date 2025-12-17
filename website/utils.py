def xor_process(input_path, output_path, key):
    """
    Reads a file, applies XOR encryption/decryption using the key,
    and saves the result to the output_path.
    """
    # 1. Read the input file as binary data
    try:
        with open(input_path, 'rb') as fin:
            data = bytearray(fin.read())
    except FileNotFoundError:
        return False

    # 2. Prepare the key
    # We convert the password string (e.g., "download") into bytes
    key_bytes = bytearray(key, 'utf-8') 
    key_len = len(key_bytes)

    # 3. The Math (XOR Operation)
    # We loop through every byte of the image and XOR it with the key
    for i in range(len(data)):
        data[i] ^= key_bytes[i % key_len]

    # 4. Save the new "scrambled" (or unscrambled) file
    with open(output_path, 'wb') as fout:
        fout.write(data)
    
    return True