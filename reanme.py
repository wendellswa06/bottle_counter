import os
import glob

def rename_images(folder_path):
    
    os.chdir(folder_path)
    
    image_files = glob.glob("*.jpg") + glob.glob("*.jpeg") + glob.glob("*.png")
    
    image_files.sort()
    
    counter = 1
    
    for old_name in image_files:
        extension = os.path.splitext(old_name)[1]
        print(extension)
        new_name = f'thumbsup_{counter}{extension}'
        
        os.rename(old_name, new_name)
        counter += 1
        
if __name__ == '__main__':
    BASE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "images")
    folders = [os.path.join(BASE_DIR, f) for f in os.listdir(BASE_DIR) if os.path.isdir(os.path.join(BASE_DIR, f))]
    print(folders)
    for folder_path in folders:
        rename_images(folder_path)