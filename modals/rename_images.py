import os

def rename_images():
    # Get the name of the current directory
    current_directory = os.path.basename(os.getcwd())
    
    # Get a list of all files in the current directory
    files = os.listdir()
    
    # Filter out only image files
    image_files = [file for file in files if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.webp'))]
    
    # Rename image files based on folder name
    if current_directory == "stories":
        prefix = "storie"
    elif current_directory == "gallery":
        prefix = "image"
    elif current_directory == "shop":
        prefix = "product"
    else:
        print("Unknown folder name. Images not renamed.")
        return
    
    for i, filename in enumerate(image_files, start=1):
        new_filename = f"{prefix}_{i}.{filename.split('.')[-1]}"
        os.rename(filename, new_filename)
        print(f"Renamed '{filename}' to '{new_filename}'")

if __name__ == "__main__":
    rename_images()
