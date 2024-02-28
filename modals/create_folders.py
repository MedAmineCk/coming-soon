import os

def create_folders():
    # Define folder names
    folders = ['gallery', 'stories', 'shop']
    
    # Create folders if they do not exist
    for folder in folders:
        if not os.path.exists(folder):
            os.makedirs(folder)
            print(f"Folder '{folder}' created successfully.")
        else:
            print(f"Folder '{folder}' already exists.")

if __name__ == "__main__":
    create_folders()
