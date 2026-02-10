from stegano import lsb
import os

# Function to get the correct path regardless of where terminal is
def get_file_path(filename):
    # Get the folder where THIS script is currently sitting
    script_folder = os.path.dirname(os.path.abspath(__file__))
    # Join it with the filename
    return os.path.join(script_folder, filename)

def hide_message():
    filename = input("Enter the name of your image file (e.g., secret.png): ")
    image_path = get_file_path(filename)
    
    print(f"DEBUG: Looking for image here -> {image_path}")
    
    # Check if file actually exists before crashing
    if not os.path.exists(image_path):
        print("ERROR: Could not find that file! Check the name again.")
        return

    secret_text = input("Enter the secret message to hide: ")
    secret = lsb.hide(image_path, secret_text)
    
    # Save in the same folder
    save_path = get_file_path("secret_image.png")
    secret.save(save_path)
    print(f"SUCCESS: Message hidden! Saved as -> {save_path}")

def reveal_message():
    filename = input("Enter the file to decrypt (e.g., secret_image.png): ")
    image_path = get_file_path(filename)
    
    try:
        clear_message = lsb.reveal(image_path)
        print(f"DECRYPTED MESSAGE: {clear_message}")
    except:
        print("No secret message found in this image!")

# --- MENU ---
if __name__ == "__main__":
    print("--- PROJECT ENIGMA (GPS ENABLED) ---")
    print("1. Hide a Message")
    print("2. Read a Message")
    choice = input("Choose (1 or 2): ")
    
    if choice == '1':
        hide_message()
    elif choice == '2':
        reveal_message()
    else:
        print("Invalid choice.")