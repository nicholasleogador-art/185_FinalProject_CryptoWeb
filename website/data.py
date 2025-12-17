# The "Mock" Database for the puzzles
# hint_text: What the user sees
# password: What the user must type to solve it

puzzles_db = [
    {
        'id': 1,
        'name': 'James Ceaser',
        'type': 'text',
        'hint_text': 'Wkh sdvvzrug lv: Vhfuhw', # "The password is: Secret" (Shift -3)
        'password': 'Secret', 
        'success_message': 'MISSION ACCOMPLISHED: The mole is in the park.'
    },
    {
        'id': 2,
        'name': 'Bin Askal',
        'type': 'text',
        'hint_text': '01001000 01100101 01101100 01101100 01101111', # "Hello" in Binary
        'password': 'Hello',
        'success_message': 'SYSTEM ACCESS GRANTED: The binary gateway is open.'
    },
    {
        'id': 3,
        'name': 'Classified Image',
        'type': 'image',
        'hint_text': 'Enter access code to decrypt file.',
        'password': 'T7GApsTS', 
        # The scrambled file sitting on your server
        'encrypted_filename': 'encrypted_image.bin', 
        # What the file will be named when the user downloads it
        'decrypted_filename': 'secret_evidence.png' 
    }
]