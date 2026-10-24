import os
import shutil
from pathlib import Path

# Define the category mapping dictionary for file extensions
EXTENSION_MAPPING = {
    # Documents
    '.pdf': 'Documents',
    '.docx': 'Documents',
    '.doc': 'Documents',
    '.txt': 'Documents',
    '.xlsx': 'Documents',
    '.csv': 'Documents',
    '.pptx': 'Documents',
    
    # Images
    '.jpg': 'Images',
    '.jpeg': 'Images',
    '.png': 'Images',
    '.gif': 'Images',
    '.bmp': 'Images',
    '.svg': 'Images',
    
    # Videos
    '.mp4': 'Videos',
    '.mkv': 'Videos',
    '.avi': 'Videos',
    '.mov': 'Videos',
    
    # Archives
    '.zip': 'Archives',
    '.rar': 'Archives',
    '.tar': 'Archives',
    '.gz': 'Archives',
    '.7z': 'Archives',
    
    # Code / Scripts
    '.py': 'Code',
    '.js': 'Code',
    '.html': 'Code',
    '.css': 'Code',
    '.cpp': 'Code',
    '.java': 'Code',
    '.json': 'Code'
}

def get_unique_destination(dest_path):
    """
    Handles naming collisions by appending an incremental suffix 
    if a file with the same name already exists in the destination folder.
    """
    if not dest_path.exists():
        return dest_path
    
    base = dest_path.stem
    suffix = dest_path.suffix
    parent = dest_path.parent
    counter = 1
    
    while True:
        new_name = f"{base}_{counter}{suffix}"
        new_path = parent / new_name
        if not new_path.exists():
            return new_path
        counter += 1

def organize_directory(target_dir_path):
    target_path = Path(target_dir_path)
    
    if not target_path.exists() or not target_path.is_dir():
        print(f"⚠️ Error: The directory '{target_dir_path}' does not exist or is not a valid directory.")
        return

    print("==================================================")
    print("   DATHEON DESKTOP FILE ORGANIZER UTILITY        ")
    print("==================================================")
    print(f"Target Directory: {target_path.resolve()}\n")

    moved_count = 0
    skipped_count = 0
    error_count = 0

    # Use os.scandir() via pathlib/iterator for efficiency
    try:
        with os.scandir(target_path) as entries:
            for entry in entries:
                # Skip directories, only organize files
                if entry.is_dir():
                    continue
                
                file_path = Path(entry.path)
                file_ext = file_path.suffix.lower()
                
                # Determine category based on extension mapping (default to 'Others' if unknown)
                category = EXTENSION_MAPPING.get(file_ext, 'Others')
                
                # Create category subfolder dynamically if it doesn't exist
                category_dir = target_path / category
                try:
                    category_dir.mkdir(exist_ok=True)
                except PermissionError:
                    print(f"❌ Permission Denied: Could not create folder '{category}'.")
                    error_count += 1
                    continue

                # Target file path inside the category subfolder
                dest_path = category_dir / file_path.name
                final_dest_path = get_unique_destination(dest_path)

                # Safely move the file using shutil.move
                try:
                    shutil.move(str(file_path), str(final_dest_path))
                    print(f"📦 Moved: {file_path.name} ➔ /{category}/{final_dest_path.name}")
                    moved_count += 1
                except PermissionError:
                    print(f"❌ Permission Error: Access denied when moving '{file_path.name}'.")
                    error_count += 1
                except Exception as e:
                    print(f"⚠️ Error moving '{file_path.name}': {e}")
                    error_count += 1

    except Exception as e:
        print(f"⚠️ An error occurred while scanning the directory: {e}")

    # Print a formatted execution summary
    print("\n" + "="*50)
    print("             ORGANIZATION SUMMARY                 ")
    print("="*50)
    print(f" Total Files Relocated : {moved_count}")
    print(f" Errors Encountered    : {error_count}")
    print("="*50)

if __name__ == "__main__":
    # You can specify any path here (e.g., r"C:\Users\DELL\Downloads")
    # For safety during testing, it defaults to a local test folder or current directory input.
    user_input_path = input("Enter the full path of the directory to organize (or press Enter for current folder): ").strip()
    
    if not user_input_path:
        target_directory = "."
    else:
        target_directory = user_input_path.strip('"') # Strip quotes if user dragged and dropped folder path
        
    organize_directory(target_directory)