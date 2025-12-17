from flask import Blueprint, render_template, request, flash, current_app, Response, url_for
from .data import puzzles_db
from .utils import xor_process 
import os

auth = Blueprint('auth', __name__)

@auth.route('/login/<int:user_id>', methods=['GET', 'POST'])
def puzzle_login(user_id):
    puzzle = next((p for p in puzzles_db if p['id'] == user_id), None)
    
    if not puzzle:
        return "Account not found", 404

    if request.method == 'POST':
        user_input = request.form.get('password')

        if user_input == puzzle['password']:
            
            # === SCENARIO 1: IMAGE ACCOUNT (ID 3) ===
            if puzzle['type'] == 'image':
                
                # 1. Define paths (We use current_app to find the exact folder)
                static_folder = os.path.join(current_app.root_path, 'static', 'images')
                
                # FIX: Use 'encrypted_filename' instead of 'filename'
                encrypted_path = os.path.join(static_folder, puzzle['encrypted_filename'])
                decrypted_filename = 'unlocked_secret.png'
                decrypted_path = os.path.join(static_folder, decrypted_filename)

                # 2. Run Decryption
                if xor_process(encrypted_path, decrypted_path, user_input):
                    flash('Decryption Successful.', 'success')
                    # Render the Success Page instead of downloading immediately
                    return render_template('success_image.html', image_name=decrypted_filename)
                else:
                    flash("Error: Encrypted source file missing from server.", "error")

            # === SCENARIO 2: TEXT ACCOUNTS (ID 1 & 2) ===
            elif puzzle['type'] == 'text':
                content = f"User: {puzzle['name']}\n------------------\n{puzzle['success_message']}"
                return Response(
                    content,
                    mimetype="text/plain",
                    headers={"Content-disposition": f"attachment; filename={puzzle['name']}_clue.txt"}
                )

        else:
            flash('Access Denied: Incorrect Decryption Key', 'error')

    return render_template('login_puzzle.html', puzzle=puzzle)

# --- NEW FUNCTION: DOWNLOAD MISSION LOG ---
@auth.route('/download_log/<int:user_id>')
def download_log(user_id):
    puzzle = next((p for p in puzzles_db if p['id'] == user_id), None)
    
    if puzzle:
        log_content = (
            f"TARGET ID: {puzzle['id']}\n"
            f"TARGET NAME: {puzzle['name']}\n"
            f"STATUS: SYSTEM PENETRATED\n"
            f"----------------------------------------\n"
            f"Encryption bypassed successfully.\n"
            f"Asset recovered.\n"
            f"Access Timestamp: APPROVED\n"
        )
        return Response(
            log_content,
            mimetype="text/plain",
            headers={"Content-disposition": f"attachment; filename=mission_report_{user_id}.txt"}
        )
    return "Error: Log not found", 404